import os
import sys
import argparse
from PIL import Image

def convert_webp_to_jpg(input_directory, output_directory=None):
    # Check if the input directory exists
    if not os.path.exists(input_directory):
        print(f"The input directory {input_directory} does not exist.")
        return

    # Create the output directory if it doesn't exist
    if output_directory and not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".webp"):
            webp_path = os.path.join(input_directory, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(output_directory if output_directory else input_directory, jpg_filename)

            if os.path.exists(jpg_path):
                print(f"Skipping {filename}: {jpg_filename} already exists")
                continue

            try:
                # Open the .webp file
                with Image.open(webp_path) as img:
                    # Convert to RGB mode and save as .jpg
                    img.convert("RGB").save(jpg_path, "JPEG")
                print(f"Converted {filename} to {os.path.basename(jpg_path)}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .webp files to .jpg format.")
    parser.add_argument("input_directory", help="The directory containing .webp files.")
    parser.add_argument("-o", "--output_directory", help="The directory to save the converted .jpg files.")
    args = parser.parse_args()

    convert_webp_to_jpg(args.input_directory, args.output_directory)
