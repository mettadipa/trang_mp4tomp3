# Video to MP3 Converter (For Trang Bua)

Utilities for batch converting `.mp4` videos into `.mp3` audio files using FFmpeg.

## Requirements
- Python 3.8 or newer
- [FFmpeg](https://ffmpeg.org/) available on your `PATH`
- Python dependencies: `tqdm`

Install the Python dependency:

```bash
python -m pip install tqdm
```

## Usage
1. Place your source videos inside the `videos/` directory (or any folder you prefer).
2. Run the converter script:

```bash
python convert_folder.py
```

By default the script:
- Reads `.mp4` files from `./videos`
- Writes converted `.mp3` files to `./mp3`
- Skips files that already exist in the destination folder
- Uses a `192k` audio bitrate

## Customising the conversion
You can call the conversion function directly to override the defaults:

```python
from convert_folder import convert_all_mp4_to_mp3_ffmpeg

convert_all_mp4_to_mp3_ffmpeg(
    input_folder="path/to/videos",
    output_folder="path/to/output",
    overwrite=True,
    bitrate="256k",
)
```

Parameters:
- `input_folder`: Directory containing `.mp4` files.
- `output_folder`: Directory for output `.mp3` files. When `None`, uses the input folder.
- `overwrite`: If `False`, existing audio files are left untouched.
- `bitrate`: Target audio bitrate passed to FFmpeg (e.g. `128k`, `192k`, `256k`).

## Notes
- Progress is displayed with a command-line progress bar powered by `tqdm`.
- FFmpeg errors are reported per file; successful conversions are silent unless `overwrite` is triggered.
- Generated audio and video files are ignored by Git via `.gitignore`.
