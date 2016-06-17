from timer import *
timer = timer()
import numpy as np
from licker import *
#from subj import Sessions, Trials, Licks
from stimulus import *
import pygame


import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)

# Set Parameters
w = 405
h = 270
trial = 1
max_trials = 1
RP = 2
ITI = 2

# Set images
GO_images = ('images/obj1_01.jpeg', 'images/obj1_02.jpeg')
NOGO_images = ('images/obj2_01.jpeg', 'images/obj2_02.jpeg')

#GO_images = ("images/obj1_01.jpeg", "images/obj1_02.jpeg", "images/obj1_03.jpeg", "images/obj1_04.jpeg", "images/obj1_05.jpeg", "images/obj1_06.jpeg", "images/obj1_07.jpeg", "images/obj1_08.jpeg", "images/obj1_09.jpeg", "images/obj1_10.jpeg", "images/obj1_11.jpeg", "images/obj1_12.jpeg", "images/obj1_13.jpeg", "images/obj1_14.jpeg", "images/obj1_15.jpeg", "images/obj1_16.jpeg", "images/obj1_17.jpeg", "images/obj1_18.jpeg", "images/obj1_19.jpeg", "images/obj1_20.jpeg")
#NOGO_images = ("images/obj2_01.jpeg", "images/obj2_02.jpeg", "images/obj2_03.jpeg", "images/obj2_04.jpeg", "images/obj2_05.jpeg", "images/obj2_06.jpeg", "images/obj2_07.jpeg", "images/obj2_08.jpeg", "images/obj2_09.jpeg", "images/obj2_10.jpeg", "images/obj2_11.jpeg", "images/obj2_12.jpeg", "images/obj2_13.jpeg", "images/obj2_14.jpeg", "images/obj2_15.jpeg", "images/obj2_16.jpeg", "images/obj2_17.jpeg", "images/obj2_18.jpeg", "images/obj2_19.jpeg", "images/obj2_20.jpeg")

# Initialize image matrices
GO_resp = np.ones(np.size(GO_images))
NOGO_resp = np.zeros(np.size(NOGO_images))
ALL_images = GO_images + NOGO_images
ALL_resp = np.concatenate([GO_resp, NOGO_resp])

# Load images
stim = stimulus(ALL_images, w, h)

# Datajoin stuff
timer.start()
#session = dict(mouse_id=1, session_tmst=timer.start_time)
#Sessions().insert1(session)

# Initialize other settings
stim.init_block()
trial = 0
state_time = 0

# RUN
while trial < max_trials:  # Each trial is one block

    for istim in range(stim.block_sz):
        index = stim.init_trial()
        corr_resp = ALL_resp[index] == 1
 #       trial_key = dict(trial_tmst=timer.time())
 #       Trials().insert1(dict(session, **trial_key))

        # Show Stimulus
        stim.show()

        # Start countdown for response
        timer.start()
        while timer.elapsed_time() < RP:  # response period
            if licker().lick():
 #               lick_key = dict(lick_tmst=timer.time())
 #               Licks().insert1(dict(session, **lick_key))
                print('Correct!' if corr_resp else 'Wrong')
                if corr_resp:
                    stim.color([88, 128, 88])
                else:
                    stim.color([128, 88, 88])

                break
        else:  # no lick case
            print('Wrong!' if corr_resp else 'Correct!')
            if corr_resp:
                stim.color([128, 88, 88])
            else:
                stim.color([88, 128, 88])
        stim.unshow()
        timer.start()
        while timer.elapsed_time() < ITI:
            if licker().lick():
  #              lick_key = dict(lick_tmst=timer.time())
          #      Licks().insert1(dict(session, **lick_key))
                timer.start()
                print('wait!')
                stim.color([88, 88, 88])
                stim.unshow()

    trial += 1
