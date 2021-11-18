from game.action import Action
from game import constants
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        ball = cast['balls'][0]
        for group in cast:
            if group == 'balls':
                position = ball.get_position()
                velocity = ball.get_velocity()
                if position.get_x() >= constants.MAX_X:
                    ball.set_velocity(Point((velocity.get_x() * -1), velocity.get_y()))
                    
                elif position.get_y() >= constants.MAX_Y:
                    ball.set_velocity(Point(velocity.get_x(), (velocity.get_y() * -1)))
                    
                


