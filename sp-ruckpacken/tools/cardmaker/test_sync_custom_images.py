"""Gezielte Regressionstests für Bildzuordnung, Vorrang und Wiederholbarkeit."""

import contextlib
import csv
import io
import shutil
import tempfile
import unittest
from pathlib import Path

from build_cm_data import active_image_path
from sync_custom_images import discover_custom, plan_sync, synchronize


class CustomImagesTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ruckpacken-images-")
        self.addCleanup(self.temporary.cleanup)
        self.game = Path(self.temporary.name)
        original = Path(__file__).resolve().parents[2]
        self.cm = self.game / "tools/cardmaker"
        self.assets = self.game / "assets/img/objects"
        self.assets.mkdir(parents=True)
        for relative in (
            "files/data/ruckpacken_74.csv",
            "tools/cardmaker/assets/images/arasaac/sources.csv",
            "tools/cardmaker/cards.csv",
        ):
            target = self.game / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original / relative, target)
        self.fallback = (original / "tools/cardmaker/assets/images/arasaac/color/sym_01.png").read_bytes()
        self.custom = (original / "assets/img/objects/rp1_ball.png").read_bytes()
        for number in range(1, 74):
            target = self.cm / f"assets/images/arasaac/color/sym_{number:02}.png"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.fallback)

    def pair(self, stem="rp1_ball", suffix=".concepts"):
        (self.assets / f"{stem}.png").write_bytes(self.custom)
        (self.assets / f"{stem}{suffix}").write_bytes(b"Concepts source fixture")

    def sync(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return synchronize(self.game, **kwargs)

    def test_custom_priority_csv_and_card_identity(self):
        self.pair()
        (self.assets / "_Size_709x709__Line_17-5px.txt").touch()
        with (self.cm / "cards.csv").open(encoding="utf-8-sig", newline="") as handle:
            before = list(csv.DictReader(handle))
        self.assertEqual(self.sync(), 0)
        self.assertEqual((self.cm / "assets/images/sym_1.png").read_bytes(), self.custom)
        self.assertEqual((self.cm / "assets/images/custom/sym_1.png").read_bytes(), self.custom)
        self.assertEqual((self.cm / "assets/images/sym_2.png").read_bytes(), self.fallback)
        with (self.game / "files/data/custom-img_mapping.csv").open(encoding="utf-8-sig", newline="") as handle:
            mapping = list(csv.DictReader(handle))
        self.assertEqual(len(mapping), 73)
        self.assertEqual(mapping[0]["Gegenstand"], "Ball")
        self.assertEqual(mapping[0]["Concepts"], "assets/img/objects/rp1_ball.concepts")
        self.assertEqual([row["Quelle"] for row in mapping], ["custom"] + ["arasaac"] * 72)
        with (self.cm / "cards.csv").open(encoding="utf-8-sig", newline="") as handle:
            after = list(csv.DictReader(handle))
        for old, new in zip(before, after, strict=True):
            self.assertEqual(new["card_id"], old["card_id"])
            self.assertEqual(new["Count"], old["Count"])
            for slot in range(1, 10):
                key = f"slot_{slot:02}"
                self.assertEqual(new[key], active_image_path(old[key]))

    def test_repeat_new_pair_and_removed_pair(self):
        self.pair()
        self.sync()
        outputs, _, _ = plan_sync(self.game)
        modified = {path: path.stat().st_mtime_ns for path in outputs}
        self.assertEqual(self.sync(check=True), 0)
        self.sync()
        self.assertEqual(modified, {path: path.stat().st_mtime_ns for path in outputs})
        self.pair("rp2_besen", ".conzepts")
        self.assertEqual(self.sync(check=True), 1)
        self.assertEqual(self.sync(dry_run=True), 0)
        self.assertEqual((self.cm / "assets/images/sym_2.png").read_bytes(), self.fallback)
        self.sync()
        self.assertEqual((self.cm / "assets/images/sym_2.png").read_bytes(), self.custom)
        (self.assets / "rp1_ball.concepts").unlink()
        self.sync()
        self.assertEqual((self.cm / "assets/images/sym_1.png").read_bytes(), self.fallback)

    def test_incomplete_pair_does_not_replace_fallback(self):
        (self.assets / "rp1_ball.png").write_bytes(self.custom)
        outputs, warnings, count = plan_sync(self.game)
        self.assertEqual(count, 0)
        self.assertEqual(len(warnings), 1)
        self.assertEqual(outputs[self.cm / "assets/images/sym_1.png"], self.fallback)

    def test_mismatched_number_and_duplicate_fail_before_writing(self):
        self.pair("rp2_ball")
        with self.assertRaisesRegex(RuntimeError, "passen nicht"):
            self.sync()
        self.assertFalse((self.cm / "assets/images/sym_1.png").exists())
        (self.assets / "rp2_ball.png").unlink()
        (self.assets / "rp2_ball.concepts").unlink()
        self.pair()
        self.pair("Ball")
        with self.assertRaisesRegex(RuntimeError, "Mehrere Bilder"):
            self.sync()

    def test_missing_fallback_does_not_write_partial_outputs(self):
        self.pair()
        (self.cm / "assets/images/arasaac/color/sym_73.png").unlink()
        with self.assertRaises(OSError):
            self.sync()
        self.assertFalse((self.cm / "assets/images/sym_1.png").exists())

    def test_umlaut_name_and_legacy_windows_paths(self):
        self.pair("rp35_massband")
        found, warnings = discover_custom(self.assets, {35: "Maßband"})
        self.assertEqual(list(found), [35])
        self.assertEqual(warnings, [])
        self.assertEqual(active_image_path(r"assets\images\arasaac\color\sym_01.png"), "assets/images/sym_1.png")
        with self.assertRaises(RuntimeError):
            active_image_path("sym_74.png")


if __name__ == "__main__":
    unittest.main()
