## Nabu

A helper program to detect, split and rebuild interesting parts of long videos.


### Dependencies

- MPV
- Python3

## Usage

Use mpv-time.sh to and find the moments you want to return to.
It will start a mpv file loaded with the script time.lua which
let you choose a moment and save it to a .log file (specifically videopath/videoname.videoextension.log)

Use main_refine.py to choose trim start and end points. This python script
will iterate over said log file and take you there with a mpv loaded with
refine.lua which will let you choose start time with key **s** and choose
end time with key **d**. After finished choosing by pressing enter those
times will save to a timestamp file (specifically videopath/videoname.videoextension.timestamp)

Use trim.py to trim given start and end points. Trim.py will iterate over said timestamp file and will trim chosen times. It saves them as 'videopath/videoname.videoextension.**index**.mp4'

./mpv-time.sh name_of_the_video.mp4
./main_refine.py name_of_the_video.mp4 name_of_the_video.mp4.log
./trim.py name_of_the_video.mp4 name_of_the_video.mp4.timestamp



## TODO

[ ] - Consider other video extensions
