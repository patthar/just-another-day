#!/usr/bin/env python
 
import sys
import time
import RPi.GPIO as io
import subprocess
 
io.setwarnings(False)
io.setmode(io.BOARD)
SHUTOFF_DELAY = 60 * 5  # seconds
PIR_PIN = 7         
log_file = open("/tmp/detect_and_fire.log", "w")
 
def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = True
    last_motion_time = time.time()
    subprocess.call("sh -c export DISPLAY=:0 && cd /home/pi/projects/just-another-day && python /home/pi/projects/just-another-day/smartmirror.py", shell=True)
 
    while True:
        if io.input(PIR_PIN):
	    last_motion_time = time.time()
	    print("on - %f" % last_motion_time)
	    log_file.write("on - %f\n" % last_motion_time)
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
	    print("off - %f" % last_motion_time)
	    log_file.write("off - %f\n" % last_motion_time)
            if not turned_off and time.time() >= (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
        time.sleep(1)
 
def turn_on():
    print("turning on.......please wait\n")
    log_file.write("turning on.......please wait\n")
    subprocess.call("sh -c export DISPLAY=:0 && /home/pi/projects/just-another-day/monitor-on.sh", shell=True)
 
def turn_off():
    print("turning OFF.......please wait\n")
    log_file.write("turning OFF.......please wait\n")
    subprocess.call("sh /home/pi/projects/just-another-day/monitor-off.sh", shell=True)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
