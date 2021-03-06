from stimulus import *
import numpy as np
import time
from matplotlib import pyplot

GO_images = ('image1.jpg', 'image2.jpg')
NOGO_images = ('image3.jpg', 'image4.jpg')

# Initialize image matrices
GO_resp = np.ones(np.size(GO_images))
NOGO_resp = np.zeros(np.size(NOGO_images))
ALL_images = GO_images + NOGO_images
ALL_resp = np.concatenate([GO_resp, NOGO_resp])

pygame.init()
clock = pygame.time.Clock()
FPS = 60
s = stimulus(ALL_images)
s.init_block()

stimes = np.zeros(200)
etimes = np.zeros(200)
for itrial in range(200):
    stimes[itrial] = time.time()
    s.init_trial()
    s.show()
    clock.tick(FPS)
    s.unshow()
    etimes[itrial] = time.time()

times = etimes - stimes
s.close()


pyplot.hist(times,100)
pyplot.show()