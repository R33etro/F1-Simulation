

class Bolide:
    
    """
    Class that represents a bolide object
    """

    def __init__(self, name, speed, skill, strategy):
        
        """Constructor of the Bolide's class.
            Initializes the bolide object
        Args:
            name : name of the bolide
            speed : speed of the bolide
            skill : skill of the bolide
            strategy : strategy of the bolide
            speed, skill, strategy : float - values between 0 and 1; factors that determine the bolide's performance"""
        
        self.name = name
        self.speed = speed
        self.skill = skill
        self.strategy = strategy
        self.lap_time = 0
        self.progress = 0
        self.gap = 0
       