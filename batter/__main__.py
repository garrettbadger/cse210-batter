import os

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

# TODO: Add imports similar to the following when you create these classes
# from game.brick import Brick
# from game.ball import Ball
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    
    # TODO: Create bricks here and add them to the list
    
    bricks = []
    for x in range(20, 750, constants.BRICK_WIDTH):
        for y in range(0, 200, constants.BRICK_HEIGHT):
            brick = Brick()
            position = Point(x, y)
            brick.set_position(position)
            brick.set_image(constants.IMAGE_BRICK)
            bricks.append(brick)

            
    
    cast['bricks'] = bricks

        
        




    # brick1 = Brick()
    # brick1.set_position(Point(10,10))
    # brick1.set_image(constants.IMAGE_BRICK)
    # brick1.set_height(constants.BRICK_HEIGHT)
    # brick1.set_width(constants.BRICK_WIDTH)
    # cast["bricks"].append(brick1)
    
    # brick2 = Brick()
    # brick2.set_position(Point(100,10))
    # brick2.set_image(constants.IMAGE_BRICK)
    # brick2.set_height(constants.BRICK_HEIGHT)
    # brick2.set_width(constants.BRICK_WIDTH)
    # cast["bricks"].append(brick2)
    # brick3 = Brick()
    # brick3.set_position(Point(200,10))
    # brick3.set_image(constants.IMAGE_BRICK)
    # brick3.set_height(constants.BRICK_HEIGHT)
    # brick3.set_width(constants.BRICK_WIDTH)
    # cast["bricks"].append(brick3)

    # for brick in cast["bricks"]:
    #     print(brick.get_position()._x)
    #     print(brick.get_position()._y)


    cast["balls"] = []
    # TODO: Create a ball here and add it to the list

    cast["paddle"] = []
    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = []
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
