#!/usr/bin/env python3

import sys
import os
import subprocess as sp
from moviepy import *


WORKING_DIR = os.getcwd()

# TODO: Add a way to slice into section like if there's 100 timestamps if user wants it in 4 parts there'll videos consisting of 25 25 25 25
def print_help():
    print("usage: trim.py video.timestamp video_path")


def get_arguments():
    if len(sys.argv) != 3:
        print_help()
        sys.exit()
    filename, timestamp_file, videopath = sys.argv
    if not timestamp_file.endswith(".timestamp"):
        print("This isn't a timestamp file")
        print_help()
        sys.exit()
    return timestamp_file, videopath

def parse_timestamp(timestamp: str) -> tuple:
    start, end = timestamp.split("-")
    return start, end


def ffmpeg_trim(video: str, index: int, start: str, end: str) -> bool:
    to_run = ["ffmpeg", "-ss", start, "-to", end, "-i", video, "-c:v", "copy", "-c:a", "copy", f"{video}.{str(index)}.mp4"]
    print(to_run)
    sp.run(to_run)
    return True
    
def trim_video_by_file():
    timestamp_file, videopath = get_arguments()
    timestamp_file = os.path.join(WORKING_DIR, timestamp_file)
    videopath = os.path.join(WORKING_DIR, videopath)
    video_objects = list()
    with open(timestamp_file) as file:
        for index, timestamp in enumerate(file.readlines()):
            timestamp = timestamp.strip()
            if not timestamp: continue
            parsed_timestamp = parse_timestamp(timestamp)
            ss, to = parsed_timestamp
            video_objects.append(VideoFileClip(videopath).subclip(ss, to))
    # Build
    concatenate_videoclips(video_objects).write_videofile(f"{videopath}.final.mp4")


if __name__ == "__main__":
    trim_video_by_file()
