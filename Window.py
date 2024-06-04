import pygame
from Track import Track
from Bolide import Bolide
from FORMULA_SIMULATION import screen_width, screen_height, screen, track_width, track_height, margin

#initializing pygame
pygame.init()

clock = pygame.time.Clock()
track = Track(screen_width, screen_height, screen, track_width, track_height, margin)

#creating bolides
bolide1 = Bolide("Ferrari", 5, 1, 1, (255, 0, 0), screen, track.track_x - 50, track.track_y)
bolide2 = Bolide("Mercedes", 5, 1, 1, (192, 192, 192), screen, track.track_x - 100, track.track_y + 100)
bolide3 = Bolide("RedBull", 5, 1, 1, (0, 0, 255), screen, track.track_x + 150, track.track_y + 150)

screen.fill((50,50,50))
track.draw_track()
bolides = [bolide1, bolide2, bolide3]

run = True
#main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    for bolide in bolides:
        bolide.update()

    #cleaning the screen
    screen.fill((50, 50, 50))

    #drawing the track and bolides
    track.draw_track()

    for bolide in bolides:
        bolide.draw()

    pygame.display.update()
    clock.tick(30)  #FPS - frames per second
    

    pygame.display.update()
    

pygame.quit()
