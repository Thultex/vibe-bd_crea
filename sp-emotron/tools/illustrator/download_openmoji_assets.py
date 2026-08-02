#!/usr/bin/env python3
"""Download the ordered OpenMoji vector set for the Emotron Illustrator file."""

from __future__ import annotations

import argparse
import json
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_ROOT = REPO_ROOT / "sp-emotron" / "files" / "openmoji"

ASSETS = [
    ("0_neutral.svg", "1F610", "Neutral", "ausgeglichen", "neutral"),
    ("1_neugier_1_interessiert.svg", "1F60F", "Neugier", "interessiert", "base"),
    ("1_neugier_2_neugierig.svg", "1FAE2", "Neugier", "neugierig", "base"),
    ("1_neugier_3_fasziniert.svg", "1F929", "Neugier", "fasziniert", "base"),
    ("1-2_bewunderung.svg", "1F60D", "Neugier + Zuneigung", "Bewunderung", "combo"),
    ("2_zuneigung_1_freundlich.svg", "1F609", "Zuneigung", "freundlich", "base"),
    ("2_zuneigung_2_zugewandt.svg", "1F917", "Zuneigung", "zugewandt", "base"),
    ("2_zuneigung_3_verbunden.svg", "1F970", "Zuneigung", "verbunden", "base"),
    ("2-3_dankbarkeit.svg", "1F979", "Zuneigung + Freude", "Dankbarkeit", "combo"),
    ("3_freude_1_zufrieden.svg", "1F60C", "Freude", "zufrieden", "base"),
    ("3_freude_2_froehlich.svg", "1F60A", "Freude", "fröhlich", "base"),
    ("3_freude_3_begeistert.svg", "1F602", "Freude", "begeistert", "base"),
    ("3-4_streitlust.svg", "1F608", "Freude + Wut", "Streitlust", "combo"),
    ("4_wut_1_gereizt.svg", "1F612", "Wut", "gereizt", "base"),
    ("4_wut_2_veraergert.svg", "1F620", "Wut", "verärgert", "base"),
    ("4_wut_3_wuetend.svg", "1F92C", "Wut", "wütend", "base"),
    ("4-5_abwertung.svg", "1F644", "Wut + Ekel", "Abwertung", "combo"),
    ("5_ekel_1_abgeneigt.svg", "1F615", "Ekel", "abgeneigt", "base"),
    ("5_ekel_2_angeekelt.svg", "1F62C", "Ekel", "angeekelt", "base"),
    ("5_ekel_3_uebel.svg", "1F922", "Ekel", "übel", "base"),
    ("5-6_unbehagen.svg", "1F623", "Ekel + Scham", "Unbehagen", "combo"),
    ("6_scham_1_verlegen.svg", "1F605", "Scham", "verlegen", "base"),
    ("6_scham_2_befangen.svg", "1F633", "Scham", "befangen", "base"),
    ("6_scham_3_beschaemt.svg", "1FAE3", "Scham", "beschämt", "base"),
    ("6-7_reue.svg", "1F61E", "Scham + Trauer", "Reue", "combo"),
    ("7_trauer_1_bedrueckt.svg", "1F641", "Trauer", "bedrückt", "base"),
    ("7_trauer_2_traurig.svg", "1F622", "Trauer", "traurig", "base"),
    ("7_trauer_3_trauernd.svg", "1F62D", "Trauer", "trauernd", "base"),
    ("7-8_aufgeben.svg", "1F629", "Trauer + Angst", "Aufgeben", "combo"),
    ("8_angst_1_besorgt.svg", "1F61F", "Angst", "besorgt", "base"),
    ("8_angst_2_aengstlich.svg", "1F628", "Angst", "ängstlich", "base"),
    ("8_angst_3_panisch.svg", "1F631", "Angst", "panisch", "base"),
    ("8-1_ueberraschung.svg", "1F632", "Angst + Neugier", "Überraschung", "combo"),
]


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "Emotron asset builder/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read()
    if b"<svg" not in payload[:1000].lower():
        raise RuntimeError(f"No SVG returned for {url}")
    destination.write_bytes(payload)


def expected_manifest() -> dict:
    manifest_assets = []
    for variant in ("color", "sw"):
        for filename, code, emotion, name, kind in ASSETS:
            manifest_assets.append(
                {
                    "variant": variant,
                    "file": f"{variant}/{filename}",
                    "code": code,
                    "emotion": emotion,
                    "name": name,
                    "kind": kind,
                }
            )
    return {
        "source": "OpenMoji",
        "sourceUrl": "https://openmoji.org/",
        "license": "CC BY-SA 4.0",
        "order": "1 Neugier, 2 Zuneigung, 3 Freude, 4 Wut, 5 Ekel, 6 Scham, 7 Trauer, 8 Angst; Zwischenemotionen verwenden x-y",
        "filesPerVariant": len(ASSETS),
        "assets": manifest_assets,
    }


def check_assets() -> None:
    expected = {filename for filename, *_ in ASSETS}
    codes = [code for _, code, *_ in ASSETS]
    if len(codes) != len(set(codes)):
        raise RuntimeError("OpenMoji codes must be unique")

    for variant in ("color", "sw"):
        target = OUTPUT_ROOT / variant
        actual = {path.name for path in target.glob("*.svg")}
        if actual != expected:
            missing = sorted(expected - actual)
            extra = sorted(actual - expected)
            raise RuntimeError(f"{variant}: missing={missing}, extra={extra}")
        for filename in sorted(expected):
            payload = (target / filename).read_bytes()
            if b"<svg" not in payload[:1000].lower():
                raise RuntimeError(f"Invalid SVG: {variant}/{filename}")

    manifest_path = OUTPUT_ROOT / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest != expected_manifest():
        raise RuntimeError("manifest.json does not match the ordered asset definition")
    print(f"OK: {len(ASSETS)} color and {len(ASSETS)} black OpenMoji SVGs")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate the prepared files without downloading")
    parser.add_argument("--codes", nargs="+", help="Download only these OpenMoji codes and refresh the manifest")
    args = parser.parse_args()
    if args.check:
        check_assets()
        return

    expected = {filename for filename, *_ in ASSETS}
    for variant, endpoint in (("color", "color"), ("sw", "black")):
        target = OUTPUT_ROOT / variant
        target.mkdir(parents=True, exist_ok=True)
        for existing in target.glob("*.svg"):
            if existing.name not in expected:
                existing.unlink()
        selected_assets = [asset for asset in ASSETS if not args.codes or asset[1] in args.codes]
        if args.codes and len(selected_assets) != len(set(args.codes)):
            raise RuntimeError("Unknown or duplicate OpenMoji code in --codes")
        for filename, code, emotion, name, kind in selected_assets:
            destination = target / filename
            download(f"https://openmoji.org/data/{endpoint}/svg/{code}.svg", destination)
    (OUTPUT_ROOT / "manifest.json").write_text(
        json.dumps(expected_manifest(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    check_assets()
    print(f"Downloaded assets to {OUTPUT_ROOT}")


if __name__ == "__main__":
    main()
