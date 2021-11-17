from game import constants
from game.actor import Actor
from game.point import Point

class Brick(Actor):
    def __init__(self):
        super().__init__()
        self._brick_image = constants.IMAGE_BRICK
        self._brick_height = constants.BRICK_HEIGHT
        self._brick_width = constants.BRICK_WIDTH

        
    
