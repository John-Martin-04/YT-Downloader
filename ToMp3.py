import os
from moviepy.editor import VideoFileClip

# Function to convert MP4 to MP3
def convert_mp4_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)

# Replace "input_folder" with the path to your folder containing MP4 files
input_folder = "E:/mus"

# Replace "output_folder" with the path to the folder where you want to save the MP3 files
output_folder = "E:/mus1"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over files in the input folder
for file in os.listdir(input_folder):
    if file.endswith(".mp4"):
        mp4_file = os.path.join(input_folder, file)
        mp3_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp3")  # Change file extension to .mp3
        convert_mp4_to_mp3(mp4_file, mp3_file)
