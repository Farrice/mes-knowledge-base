import os

output_path = "extractions/omar-eddaoudi/module_2_transcript.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

video_ids = ["Vg2dZlTTdUo", "AjYHVeLBTfw", "AfMUYl03tC8", "1kcxUhjuW_0"]

with open(output_path, "w", encoding="utf-8") as outfile:
    for vid in video_ids:
        in_path = f"extractions/transcripts/{vid}.txt"
        if os.path.exists(in_path):
            with open(in_path, "r", encoding="utf-8") as infile:
                outfile.write(f"\n\n--- TRANSCRIPT START: {vid} ---\n\n")
                outfile.write(infile.read())
                outfile.write(f"\n\n--- TRANSCRIPT END: {vid} ---\n\n")

print(f"Successfully merged transcripts into: {output_path}")
