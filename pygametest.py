import pygame
pygame.init()
screen = pygame.display.set_mode( ( 640, 64 ), pygame.DOUBLEBUF, 8 )
palette = [
    [0  , 0  , 0  ],
    [0  , 0  , 0  ],
    [255, 0  , 0  ],
    [255, 127, 0  ],
    [255, 255, 0  ],
    [0  , 255, 0  ],
    [0  , 0  , 255],
    [70 , 0  , 130],
    [238, 130, 238],
    [255, 255, 255]
]
palette += [[0, 0, 0]] * 246
screen.set_palette( palette )
screen.set_colorkey( 0 )
image0 = pygame.image.fromstring( '\x00' * 64 * 64, ( 64, 64 ), 'P' )
image0.set_palette( palette )
image0.set_colorkey( 0 )
image1 = pygame.image.fromstring( '\x00' * 64 * 32 + '\x01' * 64 * 32, ( 64, 64 ), 'P' )
image1.set_palette( palette )
image1.set_colorkey( 0 )
image2 = pygame.image.fromstring( '\x02' * 64 * 64, ( 64, 64 ), 'P' )
image2.set_palette( palette )
image2.set_colorkey( 0 )
image3 = pygame.image.fromstring( '\x03' * 64 * 64, ( 64, 64 ), 'P' )
image3.set_palette( palette )
image3.set_colorkey( 0 )
image4 = pygame.image.fromstring( '\x04' * 64 * 64, ( 64, 64 ), 'P' )
image4.set_palette( palette )
image4.set_colorkey( 0 )
image5 = pygame.image.fromstring( '\x05' * 64 * 64, ( 64, 64 ), 'P' )
image5.set_palette( palette )
image5.set_colorkey( 0 )
image6 = pygame.image.fromstring( '\x06' * 64 * 64, ( 64, 64 ), 'P' )
image6.set_palette( palette )
image6.set_colorkey( 0 )
image7 = pygame.image.fromstring( '\x07' * 64 * 64, ( 64, 64 ), 'P' )
image7.set_palette( palette )
image7.set_colorkey( 0 )
image8 = pygame.image.fromstring( '\x08' * 64 * 64, ( 64, 64 ), 'P' )
image8.set_palette( palette )
image8.set_colorkey( 0 )
special_image = pygame.Surface( ( 64, 64 ) )
special_image.set_palette( palette )
special_image.set_colorkey( 0 )
special_image.blit( image1, ( 0, 0 ) )




while True:
    screen.fill( 9 )
    screen.blit( image0, ( 0 * 64, 0 ) )
    screen.blit( image1, ( 1 * 64, 0 ) )
    screen.blit( image2, ( 2 * 64, 0 ) )
    screen.blit( image3, ( 3 * 64, 0 ) )
    screen.blit( image4, ( 4 * 64, 0 ) )
    screen.blit( image5, ( 5 * 64, 0 ) )
    screen.blit( image6, ( 6 * 64, 0 ) )
    screen.blit( image7, ( 7 * 64, 0 ) )
    screen.blit( image8, ( 8 * 64, 0 ) )
    screen.blit( special_image, ( 9 * 64, 0 ) )
    pygame.display.flip()