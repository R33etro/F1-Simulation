import pygame
from Track import Track
from FORMULA_SIMULATION import screen_width, screen_height, screen, track_width, track_height, margin

# Inicjalizacja Pygame
pygame.init()

#główna pętla gry
run = True
clock = pygame.time.Clock()
track = Track(screen_width, screen_height, screen, track_width, track_height, margin)
screen.fill((50,50,50))
track.draw_track()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

     #rysowanie
    

    pygame.display.update()
    

pygame.quit()
