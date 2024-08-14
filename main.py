import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
playerCuserPos = (0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 1250, 120, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
