import pygame
from moviepy.video.io.VideoFileClip import VideoFileClip
from mediadecoder.decoder import Decoder
FPS = 30

pygame.init()
pygame.mixer.quit

clock = pygame.time.Clock()
Decoder.load_media(Decoder,'~/Python/obj1.mov')
# movie = VideoFileClip("C:/Users/M/Desktop/test5.mov")
# movie = pygame.movie.Movie('C:/Users/M/Desktop/test4.mpg')
# screen = pygame.display.set_mode(movie.get_size(), pygame.NOFRAME)
screen = pygame.display.set_mode(Decoder.clip.size())



background = pygame.Surface(Decoder.clip.size())
screen.blit(background,(0,0))
pygame.display.update()
screen
movie_screen = pygame.Surface(Decoder.clip.size()).convert()

movie.set_display(movie_screen)

Decoder.play()


playing = True
# for i in range(1, 100):
#while clock.get_time() < movie.get_time():
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Decoder.stop()
            playing = False
            pygame.display.quit()

    screen.blit(movie_screen,(0,0))
    pygame.display.update()
    # clock.tick(FPS)

#movie.stop()
#playing = False
#pygame.display.quit()
pygame.quit()


