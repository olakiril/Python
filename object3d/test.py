from subprocess import Popen
import time

Popen(['fbcp','&'])
Popen(['omxplayer','--crop','60,0,420,270','obj1_0002.mov'])
time.sleep(5)
Popen(['killall','fbcp'])
