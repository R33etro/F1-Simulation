import pygame

class Bolide:
    """Class representing the bolide
    Attributes:
    name: str
    speed: float
    skill: float
    strategy: float
    colour: tuple
    screen
    x: int 
    y: int 
    position: Vector2
    lap_time: float
    velocity: Vector2
    bolideSurface
    
    Methods:
    draw()
    update()
    """

    bolide_width = 20  
    bolide_height = 20

    def __init__(self, name, speed, skill, strategy):
        
        """Initializes the bolide object"""
        
        self.name = name
        self.speed = speed
        self.skill = skill
        self.strategy = strategy
        self.lap_time = 0
        # self.position = 0
        # self.position = pygame.math.Vector2(x, y)
        # self.velocity = pygame.math.Vector2(speed, 0)
        # self.colour = colour
        # self.screen = screen
        # self.bolideSurface = pygame.Surface([Bolide.bolide_width, Bolide.bolide_height], pygame.SRCALPHA, 32).convert_alpha()
        # self.rect = self.bolideSurface.get_rect(topleft=(x, y))  #the position of the bolide on the screen

    # def draw(self):

    #     """Draws the bolide on the screen"""

    #     pygame.draw.rect(self.bolideSurface, self.colour, [0, 0, Bolide.bolide_width, Bolide.bolide_height])
    #     self.screen.blit(self.bolideSurface, self.rect)

    # def update(self):

    #     """Updates the position of the bolide with the velocity vector"""

    #     self.position += self.velocity
    #     self.rect.center = self.position
        
        