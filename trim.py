#!/usr/bin/env bash

import sys
import subprocess as sp

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
    with open(timestamp_file) as file:
        for index, timestamp in enumerate(file.readlines()):
            timestamp = timestamp.strip()
            if not timestamp: continue
            parsed_timestamp = parse_timestamp(timestamp)
            ffmpeg_trim(videopath, index, *parsed_timestamp)

if __name__ == "__main__":
    trim_video_by_file()
