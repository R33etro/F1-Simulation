

class Bolide:

    def __init__(self, name, speed, skill, strategy):
        
        """Initializes the bolide object"""
        
        self.name = name
        self.speed = speed
        self.skill = skill
        self.strategy = strategy
        self.lap_time = 0
        self.progress = 0
        self.gap = 0
       