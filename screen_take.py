#!/usr/bin/env python3
from PIL import ImageGrab
from datetime import datetime
import time
import sys
counter=0
absol_path="<<Path to store files>>"
while True:
    im = ImageGrab.grab()
    dt = datetime.now()
    fname = "pic_{}.{}.png".format(dt.strftime("%Y_%m_%d_%H_%M_%S"), dt.microsecond // 100000)
    im.save(absol_path+fname, 'png')
    counter=counter+1
    time.sleep(5)           #Duration in seconds after which screenshot shall be taken
    if counter>=2160:       #Counter on number of screenshots to take before closing (The default number will be achieved in 3 hours)
        sys.exit()