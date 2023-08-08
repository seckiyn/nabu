#!/usr/bin/env python3
import sys
import subprocess as sp

# TODO: Add if ss or to is null don't add them
# TODO: Exit the mpv after it's successfully executed
def print_help():
    print("usage: refine_main.py video_name.log video_path")


def get_logfile_from_arg() -> str:
    # Return the log file
    if len(sys.argv) != 3:
        print("Too less or too much argument!")
        sys.exit()
    filename, logfile, videopath = sys.argv
    if not logfile.endswith(".log"):
        print("File must be a log file")
        sys.exit()
    return logfile, videopath

def iterate_over_logfile() -> None:
    FILENAME, VIDEOPATH = get_logfile_from_arg()
    with open(FILENAME) as file:
        for time in file.readlines():
            time = time.strip()
            print(time)
            sp.run(["mpv", "--script=refine.lua",f"--start={time}", VIDEOPATH])


if __name__ == "__main__":
    iterate_over_logfile()
