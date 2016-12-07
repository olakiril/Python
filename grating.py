import pygame
import numpy as np

class grating:
    """ This class handles the moving grating presentation
    """

    def __init__(self, orientations, w=100, h=100, loc=[0, 0]):
        pygame.init()
        size = (w, h)
        self.loc = loc
        self.screen = pygame.display.set_mode(size, pygame.NOFRAME)
        self.def_surface = pygame.Surface(size)
        self.def_surface.fill([88, 88, 88])
        # self.image_h = [pygame.image.load(image) for image in images]
        self.block_sz = np.size(orientations)
        self.oris = orientations
        self.index = []

        # make linear ramp
        X0 = (np.linspace(1, w, w) / w) - .5

        # Set wavelength and phase
        freq = 5

        # Make 2D grating
        Xm, Ym = np.meshgrid(X0, X0)

        # Change orientation by adding Xm and Ym together in different proportions
        grating=np.floor(np.sin((Xm * freq * 2 * np.pi)))
        self.grating = pygame.surfarray.make_surface(grating)

        self.unshow()


    def init_block(self):
        self.index = np.random.permutation(self.block_sz)

    def init_trial(self):
        self.screen.blit(self.grating, self.loc)
        ori_idx = self.index[0]
        if np.size(self.index) > 1:
            self.index = self.index[1:]
        else:
            self.init_block()
        return self.oris[ori_idx]

    def show(self):
        pygame.display.flip()

    def unshow(self):
        self.screen.blit(self.def_surface, self.loc)
        pygame.display.flip()

    def close(self):
        pygame.quit()
