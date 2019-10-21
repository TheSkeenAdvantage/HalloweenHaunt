# Write your code here :-)
import time
import os

from gpiozero import MotionSensor
pir = MotionSensor(4)

os.system('/usr/bin/vcgencmd display_power 0')
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    os.system('/usr/bin/vcgencmd display_power 1')
    os.system('omxplayer --display=5 -o local /home/pi/Downloads/IT.mov')

    pir.wait_for_no_motion()
    #os.system('/usr/bin/vcgencmd display_power 0')
