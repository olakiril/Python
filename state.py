from timer import *
timer = timer()
import numpy as np
from licker import *
#from subj import Sessions, Trials, Licks
from stimulus import *
import pygame

# Set Parameters
w = 100
h = 100
trial = 1
max_trials = 1
RP = 2
ITI = 2

# Set images
GO_images = ('image1.jpg', 'image2.jpg')
NOGO_images = ('image3.jpg', 'image4.jpg')

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
                break
        else:  # no lick case
            print('Wrong!' if corr_resp else 'Correct!')
        stim.unshow()
        timer.start()
        while timer.elapsed_time() < ITI:
            if licker().lick():
  #              lick_key = dict(lick_tmst=timer.time())
          #      Licks().insert1(dict(session, **lick_key))
                timer.start()
                print('wait!')

    trial += 1
