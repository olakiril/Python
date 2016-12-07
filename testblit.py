from pygame.locals import *
from pipeline import vis
import io, imageio, pygame, sys
import numpy as np

key = dict([('movie_name', 'madmax'), ('clip_number', 1)])
clip_info = (vis.Movie.Clip()*vis.Movie() & key).fetch1()
vid = imageio.get_reader(io.BytesIO(clip_info['clip'].tobytes()), 'ffmpeg')
vsize = (clip_info['frame_width'], clip_info['frame_height'])
ssize = (400,400)
pos = np.divide(ssize,2) - np.divide(vsize,2)
pygame.init()
screen = pygame.display.set_mode(ssize, pygame.NOFRAME, 24)

c = pygame.time.Clock()
screen.fill((128,128,128))

for iframe in range(100):  # range(vid.get_length()):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    py_image = pygame.image.frombuffer(vid.get_next_data(), vsize, "RGB")
    screen.blit(py_image,pos)
    pygame.display.update()
    c.tick_busy_loop(30)

vid.close()
