from timer import *
timer = timer()
from grating import *
import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)

# Set Parameters
w = 480
h = 320
max_trials = 1
RP = 4
ITI = 2

# Load images
stim = grating((0, 90), w, h)

# Initialize other settings
timer.start()
stim.init_block()
trial = 0
state_time = 0

# RUN
while trial < max_trials:  # Each trial is one block

    for istim in range(stim.block_sz):
        index = stim.init_trial()

        # Show Stimulus
        stim.show()

        # Start countdown for response
        timer.start()
        while timer.elapsed_time() < RP:  # response period
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    quit()
        stim.unshow()
        timer.start()

    trial += 1
