import pygame, sys, random, math
from celestialbody import Body

pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Circumgyration Destabilization")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
pygame.mixer.init()
pygame.mixer.music.load("assets/ambience.wav")
pygame.mixer.music.play()
clock = pygame.time.Clock()

stars = []
bodies = [
    Body(100000, (500, 375), (0, 0), 80, (255, 255, 128)),
    Body(10, (500, 250), (0, 0), 24, (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1))), 
    Body(100, (550, 750), (0, -100), 24, (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1))), 
    Body(10, (200, 375), (0, 0), 24, (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)))
]

for i in range(1, 101):
    random.seed(random.randint(0, 2147483647))
    stars.append([(random.randrange(0, 1000, 5), random.randrange(0, 750, 6)), random.randrange(1, 6), (255, 255, 200, 10)])

while True:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    
    if pygame.mouse.get_pressed()[0]:
        bodies.append(Body(1000, pygame.mouse.get_pos(), (0, 0), 15, (187, 187, 187)))
    

    

    screen.fill((0, 0, 0))
    for i in range(0, len(bodies)):
        otherbodies = bodies[:i] + bodies[i+1:]
        bodies[i].update(otherbodies, screen)
    pygame.display.flip()
