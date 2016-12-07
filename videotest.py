import pygame

FPS = 60

pygame.init()
pygame.mixer.quit

clock = pygame.time.Clock()
# movie = pygame.movie.Movie('C:/Users/M/Documents/ffmpeg/bin/test2.mpg')''
movie = pygame.movie.Movie('~/Python/obj1.mov')
# movie = pygame.movie.Movie('C:/Users/M/Desktop/test4.mpg')
# screen = pygame.display.set_mode(movie.get_size(), pygame.NOFRAME)
screen = pygame.display.set_mode(movie.get_size())

background = pygame.Surface(movie.get_size())
screen.blit(background,(0,0))
pygame.display.update()
screen
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)

movie.play()
d

playing = True
# for i in range(1, 100):
#while clock.get_time() < movie.get_time():
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False
            pygame.display.quit()

    screen.blit(movie_screen,(0,0))
    pygame.display.update()
    clock.tick(FPS)

#movie.stop()
#playing = False
#pygame.display.quit()
pygame.quit()


