import pygame

def Main():
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    duck = pygame.image.load("ozil.jpg")
    duck_rect = duck.get_rect()
    duck_rect = duck_rect.move((10, 10))

    while True:
        for event in pygame.event.get():
            if pygame.KEYDOWN == event.type:
                if pygame.K_ESCAPE == event.key:
                    return
            if pygame.QUIT == event.type:
                return

        screen.fill((0, 0, 0))
        screen.blit(duck, duck_rect)
        pygame.display.flip()

Main()