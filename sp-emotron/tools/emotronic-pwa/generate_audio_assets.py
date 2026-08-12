#!/usr/bin/env python3
"""Generate the optional deterministic Emotronic soft WAV sound set."""

from __future__ import annotations

import json
import math
import struct
import wave
from pathlib import Path


SAMPLE_RATE = 22_050
REPO_ROOT = Path(__file__).resolve().parents[3]
AUDIO_ROOT = REPO_ROOT / "assets" / "audio" / "emotronic"

EMOTION_PATTERNS = {
    "curiosity": [[523, 659], [523, 659, 784], [659, 784, 988]],
    "affection": [[587, 740], [587, 740, 880], [740, 880, 1109]],
    "joy": [[659, 784], [659, 784, 988], [784, 988, 1175]],
    "fear": [[392, 330], [392, 330, 277], [440, 370, 294, 247]],
    "neutral": [[330]],
    "anger": [[233, 196], [330, 196, 277], [392, 247, 330, 165]],
    "sadness": [[392, 330], [440, 370, 294], [440, 349, 294, 220]],
    "shame": [[494, 440], [494, 440, 392], [523, 466, 392, 330]],
    "disgust": [[277, 247], [294, 247, 220], [330, 277, 233, 196]],
}

COMBOS = {
    "bewunderung": ("curiosity", "affection"),
    "dankbarkeit": ("affection", "joy"),
    "streitlust": ("joy", "anger"),
    "abwertung": ("anger", "disgust"),
    "unbehagen": ("disgust", "shame"),
    "reue": ("shame", "sadness"),
    "aufgeben": ("sadness", "fear"),
    "ueberraschung": ("fear", "curiosity"),
}

SPECIAL_PATTERNS = {
    "game_win": ([659, 784, 988, 1175, 1319], 3),
    "simon_start": ([392, 523, 659, 784, 988], 3),
    "game_lose": ([392, 330, 262, 196], 2),
    "life_lose": ([523, 440, 349, 294], 2),
    "life_gain": ([523, 659, 784, 1047, 1319], 3),
    "power_on": ([262, 392, 523, 784], 3),
    "power_off": ([659, 523, 392, 262], 2),
}


def step_for(level: int) -> float:
    return 0.082 if level >= 3 else 0.095 if level == 2 else 0.11


def oscillator(phase: float, waveform: str, soft: bool) -> float:
    sine = math.sin(phase)
    triangle = 2.0 / math.pi * math.asin(sine)
    if soft:
        return triangle * 0.62 + sine * 0.38
    if waveform == "square":
        return 1.0 if sine >= 0 else -1.0
    return triangle


def note_envelope(age: float, duration: float, soft: bool) -> float:
    if age < 0 or age >= duration:
        return 0.0
    attack = 0.014 if soft else 0.004
    release = 0.045 if soft else 0.012
    if age < attack:
        return age / attack
    if age > duration - release:
        tail = max(0.0, (duration - age) / release)
        return tail * tail if soft else tail
    return 1.0


def render(notes: list[int], level: int, soft: bool) -> list[float]:
    step = step_for(level)
    note_duration = step * (0.94 if soft else 0.78)
    reverb_tail = 0.18 if soft else 0.035
    total_samples = math.ceil((len(notes) - 1) * step * SAMPLE_RATE + note_duration * SAMPLE_RATE + reverb_tail * SAMPLE_RATE)
    dry = [0.0] * total_samples

    for note_index, frequency in enumerate(notes):
        start = round(note_index * step * SAMPLE_RATE)
        waveform = "square" if note_index % 2 else "triangle"
        duration_samples = round(note_duration * SAMPLE_RATE)
        for offset in range(duration_samples):
            position = start + offset
            if position >= total_samples:
                break
            age = offset / SAMPLE_RATE
            phase = 2.0 * math.pi * frequency * age
            dry[position] += oscillator(phase, waveform, soft) * note_envelope(age, note_duration, soft)

    if soft:
        wet = dry[:]
        for delay_seconds, gain in ((0.041, 0.17), (0.079, 0.10), (0.127, 0.055)):
            delay = round(delay_seconds * SAMPLE_RATE)
            for index in range(delay, total_samples):
                wet[index] += dry[index - delay] * gain
        samples = wet
    else:
        samples = dry

    target_peak = 0.62 if soft else 0.72
    peak = max((abs(value) for value in samples), default=1.0) or 1.0
    gain = target_peak / peak
    fade_samples = max(1, round((0.05 if soft else 0.012) * SAMPLE_RATE))
    for index in range(total_samples):
        samples[index] *= gain
        remaining = total_samples - index
        if remaining < fade_samples:
            samples[index] *= remaining / fade_samples
    return samples


def write_wav(path: Path, samples: list[float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frames = bytearray()
    for sample in samples:
        value = max(-1.0, min(1.0, sample))
        frames.extend(struct.pack("<h", round(value * 32_767)))
    with wave.open(str(path), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        output.writeframes(frames)


def sound_specs() -> list[dict]:
    specs: list[dict] = []
    for key, levels in EMOTION_PATTERNS.items():
        for index, notes in enumerate(levels, start=1):
            specs.append({"id": f"emotion_{key}_{index}", "kind": "emotion", "notes": notes, "level": index})
    for name, (first, second) in COMBOS.items():
        first_notes = EMOTION_PATTERNS[first][2]
        second_notes = EMOTION_PATTERNS[second][2]
        notes = [first_notes[0], second_notes[0], first_notes[-1], second_notes[-1]]
        specs.append({"id": f"combo_{name}", "kind": "combo", "notes": notes, "level": 3})
    for name, (notes, level) in SPECIAL_PATTERNS.items():
        specs.append({"id": f"special_{name}", "kind": "special", "notes": notes, "level": level})
    return specs


def main() -> None:
    specs = sound_specs()
    expected_files = {f"{spec['id']}.wav" for spec in specs}
    for set_name, soft in (("8-bit_soft", True),):
        set_path = AUDIO_ROOT / set_name
        set_path.mkdir(parents=True, exist_ok=True)
        for old_file in set_path.glob("*.wav"):
            if old_file.name not in expected_files:
                old_file.unlink()
        for spec in specs:
            write_wav(set_path / f"{spec['id']}.wav", render(spec["notes"], spec["level"], soft))

    manifest = {
        "version": 1,
        "defaultPlayback": "classic",
        "optionalSet": "8-bit_soft",
        "sampleRate": SAMPLE_RATE,
        "sets": ["8-bit_soft"],
        "sounds": specs,
    }
    AUDIO_ROOT.mkdir(parents=True, exist_ok=True)
    (AUDIO_ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(specs)} sounds in {AUDIO_ROOT / '8-bit_soft'}")


if __name__ == "__main__":
    main()
