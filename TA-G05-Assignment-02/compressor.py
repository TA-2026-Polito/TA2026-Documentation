from __future__ import annotations

import subprocess
import sys
from pathlib import Path


VIDEO_EXTENSIONS = {
	".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v", ".flv", ".wmv"
}


def is_media_file(path: Path) -> bool:
	return path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS


def build_output_path(input_path: Path, output_dir: Path) -> Path:
	return output_dir / f"{input_path.stem}_compressed.mp4"


def compress_file(input_path: Path, output_path: Path) -> None:
	output_path.parent.mkdir(parents=True, exist_ok=True)

	cmd = [
		"ffmpeg",
		"-y",
		"-i",
		str(input_path),
		"-c:v",
		"libx264",
		"-preset",
		"slow",
		"-crf",
		"28",
		"-c:a",
		"aac",
		"-b:a",
		"128k",
		str(output_path),
	]

	print(f"Compressing: {input_path.name}")
	subprocess.run(cmd, check=True)


def main() -> int:
	base_dir = Path(__file__).resolve().parent
	input_dir = base_dir / "consegna_files/vid"
	output_dir = base_dir / "consegna_compressed"

	if not input_dir.exists():
		print(f"Input folder not found: {input_dir}")
		return 1

	files = [p for p in input_dir.rglob("*") if is_media_file(p)]
	if not files:
		print(f"No supported media files found in: {input_dir}")
		return 0

	for input_path in files:
		relative_parent = input_path.parent.relative_to(input_dir)
		output_path = build_output_path(input_path, output_dir / relative_parent)
		try:
			compress_file(input_path, output_path)
		except subprocess.CalledProcessError as exc:
			print(f"Failed to compress {input_path}: {exc}", file=sys.stderr)

	print("Done.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
