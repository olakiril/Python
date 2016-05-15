import pygame
import numpy as np

class stimulus:
    """ This class handles the stimulus presentation
    """

    def __init__(self,images,w=100,h=100,loc=[0,0]):
        pygame.init()
        size = (w, h)
        self.loc = loc
        self.screen = pygame.display.set_mode(size, pygame.NOFRAME)
        self.def_surface = pygame.Surface(size)
        self.image_h = [pygame.image.load(image) for image in images]
        self.block_sz = np.size(self.image_h)
        self.images = images
        self.unshow()

    def init_block(self):
        self.index = np.random.permutation(self.block_sz)

    def init_trial(self):
        self.screen.blit(self.image_h[self.index[0]], self.loc)
        image_idx = self.index[0]
        if np.size(self.index) > 1:
           self.index = self.index[1:]
        else:
           self.init_block()
        return image_idx

    def show(self):
        pygame.display.flip()

    def unshow(self):
        self.screen.blit(self.def_surface, self.loc)
        pygame.display.flip()

    def close(self):
        pygame.quit()
