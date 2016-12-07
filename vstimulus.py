from playMovie import *
import pygame
import numpy as np


class vstimulus:
    """ This class handles the stimulus presentation
    """

    def __init__(self, videos, w=100, h=100, loc=[0, 0]):
        pygame.init()
        self.size = (w, h)
        self.vcolor = [88, 88, 88]
        self.loc = loc
        self.screen = pygame.display.set_mode(self.size, pygame.NOFRAME)
        self.videos = videos
        self.block_sz = np.size(videos)

        self.unshow()

    def init_block(self):
        self.index = np.random.permutation(self.block_sz)

    def init_trial(self):

        image_idx = self.index[0]
        if np.size(self.index) > 1:
            self.index = self.index[1:]
        else:
            self.init_block()

        self.myVideoPlayer = VideoPlayer([480, 320], fullscreen=True, soundrenderer="pyaudio", loop=False)
        self.myVideoPlayer.load_media(self.videos[image_idx])
        self.myVideoPlayer.play()

        return image_idx

    def show(self):
        # flip
        self.myVideoPlayer.play_frame()

    def unshow(self):

        if hasattr(self, 'myVideoPlayer'):
            self.myVideoPlayer.stop()
            pygame.quit()
        #self.def_surface = pygame.Surface(self.size)
        #self.def_surface.fill(self.vcolor)
        #self.screen.blit(self.def_surface, self.loc)
        #pygame.display.flip()

    def color(self, color):
        self.vcolor = color

    def close(self):
        pygame.quit()
