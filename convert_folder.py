import os
import subprocess
from tqdm import tqdm

def convert_all_mp4_to_mp3_ffmpeg(input_folder, output_folder=None, overwrite=False, bitrate="192k"):
    """
    Efficiently converts all MP4 files in a folder to MP3 using FFmpeg.

    Args:
        input_folder (str): Folder containing .mp4 files.
        output_folder (str, optional): Destination folder for .mp3 files.
        overwrite (bool): Whether to overwrite existing files. Default: False
        bitrate (str): Target audio bitrate (e.g., '128k', '192k', '256k').
    """
    if not os.path.exists(input_folder):
        print(f"❌ Input folder not found: {input_folder}")
        return

    if not output_folder:
        output_folder = input_folder
    os.makedirs(output_folder, exist_ok=True)

    # Collect MP4 files
    mp4_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mp4')]
    if not mp4_files:
        print("⚠️ No MP4 files found.")
        return

    print(f"🎬 Found {len(mp4_files)} file(s). Starting conversion...\n")

    for file in tqdm(mp4_files, desc="Converting", unit="file"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp3")

        if os.path.exists(output_path) and not overwrite:
            print(f"⏭️  Skipped (exists): {file}")
            continue

        # Build ffmpeg command
        command = [
            "ffmpeg",
            "-y" if overwrite else "-n",   # overwrite option
            "-i", input_path,
            "-vn",                         # no video
            "-acodec", "libmp3lame",       # MP3 encoder
            "-b:a", bitrate,               # bitrate
            "-ac", "2",                    # stereo output
            output_path
        ]

        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"❌ FFmpeg error on {file}: {e}")

    print("\n✅ All conversions complete!")

if __name__ == "__main__":
    input_folder = "./videos"   # Folder containing your .mp4 files
    output_folder = "./mp3"     # Optional: leave None to use same folder
    convert_all_mp4_to_mp3_ffmpeg(input_folder, output_folder, overwrite=False, bitrate="128k")