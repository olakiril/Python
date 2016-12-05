
#import datajoint as dj
#from pipeline import vis
#import io, imageio, pygame
import pygame

#key = dict([('animal_id', 9036), ('session', 1), ('scan_idx', 3), ('psy_id', 1), ('trial_idx', 6118), ('cond_idx', 14)])
#clip_info = (vis.Trial()*vis.MovieClipCond()*vis.Movie.Clip() & key).fetch1()
#vid = imageio.get_reader(io.BytesIO(clip_info['clip'].tobytes()), 'ffmpeg')

size = (256, 144)

screen = pygame.display.set_mode(size)
pygame.init()
for iframe in range(10): #range(vid.get_length()):

#    py_image = pygame.image.frombuffer(vid.get_data(iframe), size, "RGB")
    screen.fill((0,255-iframe*10,iframe*10))
#    screen.blit(py_image, (0, 0))

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
quit()

