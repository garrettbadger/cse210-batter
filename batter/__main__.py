import os

# from batter.game import handle_off_screen_action

# from batter.game import move_actors_action

# from batter.game.constants import MAX_X

# from batter.game.constants import BRICK_HEIGHT, BRICK_WIDTH
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\flipp\cse-210-solo-checkpoints\cse210-student-solo-checkpoints\07-snake\raylib-2.0.0-Win64-mingw\raylib-2.0.0-Win64-mingw\lib'
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.brick import Brick
from game.ball import Ball
from game.move_actors_action import MoveActorsAction
from game.handle_off_screen_action import HandleOffScreenAction

# TODO: Add imports similar to the following when you create these classes

 
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
#


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    
    # TODO: Create bricks here and add them to the list
    
    bricks = []
    for x in range(20, 750, constants.BRICK_WIDTH + constants.BRICK_SPACE):
        for y in range(0, 200, constants.BRICK_HEIGHT + constants.BRICK_SPACE):
            brick = Brick()
            brick.set_height(constants.BRICK_HEIGHT)
            brick.set_width(constants.BALL_WIDTH)
            brick.set_image(constants.IMAGE_BRICK)
            position = Point(x, y)
            brick.set_position(position)
            
            bricks.append(brick)

            
    
    cast['bricks'] = bricks

        

    # cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    balls = []
    ball = Ball()
    ball.set_image(constants.IMAGE_BALL)
    ball.set_height(constants.BALL_HEIGHT)
    ball.set_width(constants.BALL_WIDTH)
    ball.set_position(Point((constants.MAX_X + 2), (constants.MAX_Y / 2)))
    ball.set_velocity(Point(constants.BALL_DX, constants.BALL_DY))
    balls.append(ball)
    
    cast['balls'] = balls

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = [move_actors_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
