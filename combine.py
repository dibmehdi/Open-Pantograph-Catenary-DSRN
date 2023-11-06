# -*- coding: utf-8 -*-
"""combine

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jeStLmpIypOcYRWTrho2yuGKPH9r0vug
"""

import os
import cv2
from google.colab import drive
from tqdm import tqdm

# Mount Google Drive
drive.mount('/content/drive')

# Set the path to the folder containing videos
videos_root_folder = "/content/drive/MyDrive/TC main/exp/Affroun/RT_AFF"

# Get a list of video files in the specified folder
video_files = [f.path for f in os.scandir(videos_root_folder) if f.is_file() and f.name.endswith(".mp4")]

# Initialize variables to store video properties
frame_width, frame_height = None, None
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Initialize the VideoWriter
combined_video_path = os.path.join(videos_root_folder, "combined_video.mp4")

# Get properties from the first video
sample_video = cv2.VideoCapture(video_files[0])
frame_width = int(sample_video.get(3))
frame_height = int(sample_video.get(4))
output_video = cv2.VideoWriter(combined_video_path, fourcc, 30, (frame_width, frame_height))
sample_video.release()

# Iterate through video files in the folder
for video_file in tqdm(video_files, desc="Processing videos"):
    video_capture = cv2.VideoCapture(video_file)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        output_video.write(frame)

    video_capture.release()

output_video.release()

# Delete individual video files
for video_file in video_files:
    os.remove(video_file)
    print(f"Deleted video: {video_file}")

print("Combined video saved:", combined_video_path)