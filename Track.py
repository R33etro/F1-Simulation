import pygame 


class Track:
    def __init__(self,screen_width, screen_height, screen, track_width, track_height, margin):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.track_width = track_width
        self.track_height = track_height
        self.margin = margin
        
    
    def draw_track(self):
        black = (0, 0, 0)
        gray = (50, 50, 50)
        white = (255, 255, 255)
        pygame.display.set_caption("Formula 1 race simulation")

        #pozycja toru (środek okna)
        track_x = (self.screen_width - self.track_width) // 2
        track_y = (self.screen_height - self.track_height) // 2
        #tor
        pygame.draw.rect(self.screen, black, [track_x - self.margin, track_y - self.margin, self.track_width + self.margin * 2, self.track_height + self.margin * 2])
        pygame.draw.rect(self.screen, gray, [track_x, track_y, self.track_width, self.track_height])
        
        
        














