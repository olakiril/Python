from timer import *
timer = timer()
import numpy as np
from licked import *
#from subj import Sessions, Trials, Licks
from stimulus import *
import pygame
import os
from glob import glob

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

# Set Parameters
w = 480
h = 320
max_trials = 1
RP = 4
ITI = 2

# Set images
GO_images = glob('images/obj1*')
NOGO_images = glob('images/obj2*')

# Initialize image matrices
GO_resp = np.ones(np.size(GO_images))
NOGO_resp = np.zeros(np.size(NOGO_images))
ALL_images = GO_images + NOGO_images
ALL_resp = np.concatenate([GO_resp, NOGO_resp])

# Load images
stim = stimulus(ALL_images, w, h)

# Datajoin stuff
#session = dict(mouse_id=1, session_tmst=timer.start_time)
#Sessions().insert1(session)

# Initialize other settings
timer.start()
stim.init_block()
trial = 0
state_time = 0
pygame.mouse.set_visible(0)

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
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quit()

            if licked().lick():
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
            if licked().lick():
  #              lick_key = dict(lick_tmst=timer.time())
          #      Licks().insert1(dict(session, **lick_key))
                timer.start()
                print('wait!')
                stim.color([88, 88, 88])
                stim.unshow()

    trial += 1
