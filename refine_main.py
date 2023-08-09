#!/usr/bin/env python3
import sys
import os
import subprocess as sp


# TODO: Add if ss or to is null don't add them
# TODO: Exit the mpv after it's successfully executed
# TODO: Find a way to do these without closing mpv(maybe just use lua script)

def print_help():
    print("usage: refine_main.py video_name.log video_path")

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

def get_logfile_from_arg() -> str:
    # Return the log file
    if len(sys.argv) != 3:
        print("Too less or too much argument!")
        print_help()
        sys.exit()
    filename, logfile, videopath = sys.argv
    if not logfile.endswith(".log"):
        print("File must be a log file")
        sys.exit()
    return logfile, videopath

def iterate_over_logfile() -> None:
    FILENAME, VIDEOPATH = get_logfile_from_arg()
    refine_lua_path = os.path.join(SCRIPT_PATH, "refine.lua")
    with open(FILENAME) as file:
        for time in file.readlines():
            time = time.strip()
            print(time)
            sp.run(["mpv", f"--script={refine_lua_path}",f"--start={time}", VIDEOPATH])


if __name__ == "__main__":
    iterate_over_logfile()
