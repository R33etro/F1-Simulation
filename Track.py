import pygame 

class Track:
    """Class representing the track
    Attributes:
    screen_width: int
    screen_height: int
    screen
    track_width: int
    track_height: int
    margin: int
    track_x: int
    track_y: int
    
    Methods:
    draw_track()
    
    """
    def __init__(self,screen_width, screen_height, screen, track_width, track_height, margin):
       
        """Initializes the track object"""
       
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.track_width = track_width
        self.track_height = track_height
        self.margin = margin
        self.track_x = (self.screen_width - self.track_width) // 2
        self.track_y = (self.screen_height - self.track_height) // 2
        
    
    def draw_track(self):
        
        """Draws the track on the screen, with a black track and a gray background"""
        
        black = (0, 0, 0)
        gray = (50, 50, 50)
        pygame.display.set_caption("Formula 1 race simulation")
        
        #draw the track
        pygame.draw.rect(self.screen, black, [self.track_x - self.margin, self.track_y - self.margin, self.track_width + self.margin * 2, self.track_height + self.margin * 2])
        pygame.draw.rect(self.screen, gray, [self.track_x, self.track_y, self.track_width, self.track_height])
        
        















