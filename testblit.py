import pygame, sys
from pygame.locals import *
import datajoint as dj
from pipeline import vis
import io, imageio

key = dict([('animal_id', 9036), ('session', 1), ('scan_idx', 3), ('psy_id', 1), ('trial_idx', 6118), ('cond_idx', 14)])
clip_info = (vis.Trial()*vis.MovieClipCond()*vis.Movie.Clip() & key).fetch1()
vid = imageio.get_reader(io.BytesIO(clip_info['clip'].tobytes()), 'ffmpeg')
size = (256, 144)

pygame.init()
screen = pygame.display.set_mode(size,0,32)

for iframe in range(100):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    py_image = pygame.image.frombuffer(vid.get_data(iframe), size, "RGB")
    screen.blit(py_image, (0, 0))
    pygame.display.update()