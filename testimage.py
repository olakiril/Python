import pygame as py
import numpy as np

py.init()

screen = py.display.set_mode((200,200))
im = py.image.load("image1.jpg")

#im = np.floor(np.random.rand(100,100)*255)

#X0 = (np.linspace(1, 100, 100) / 100) - .5

# Set wavelength and phase
#freq = 10

# Make 2D grating
#Xm, Ym = np.meshgrid(X0, X0)

# Change orientation by adding Xm and Ym together in different proportions
#thetaRad = 2 * np.pi
#im = np.floor(np.sin((Xm * freq * 2 * np.pi)))

#im = pygame.surfarray.make_surface(im)

screen.blit(im,(0,0))
py.display.flip()

