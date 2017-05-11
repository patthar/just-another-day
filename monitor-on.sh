#! /bin/bash

export LC_ALL=C
sudo tvservice -p && fbset -depth 16 && sudo /bin/chvt 6 && sudo /bin/chvt 7 && cd /home/pi/projects/just-another-day && python /home/pi/projects/just-another-day/smartmirror.py
