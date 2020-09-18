#YOU CHANGE MAZE BY SEARCHING 'MAZE' IN STAGE
stage.set_background("maze2")

def start_sprite(sprite):
    sprite.set_left(-280)
    sprite.set_top(300)
    size = sprite.get_size()
    if size >= 1:
        sprite.set_size(0.5)
    sprite.pen_down()
    sprite.pen_width(2)
    ##CHANGE PEN COLOR HERE (Any color of the rainbow)##
    sprite.set_color("green")

#REPLACE LINE 16 WITH YOUR SPRITE##
sprite = codesters.Sprite("alien1")
start_sprite(sprite)

##START YOUR ALGORITHM!##

#MANUAL SPRITE ACTION (WORKS FOR A SPECIFIC MAZE)#
sprite.move_right(140)
sprite.move_down(50)
sprite.move_right(100)
sprite.move_up(50)
sprite.move_right(100)
sprite.move_down(110)
sprite.move_right(100)
sprite.move_down(40)
sprite.move_left(150)
sprite.move_down(50)
sprite.move_right(150)

#EVENT LISTENER (WORKS FOR ANY MAZE)#
def left_key():
    sprite.move_left(20)
    # add other actions...
    
stage.event_key("left", left_key)
def right_key():
    sprite.move_right(20)
    # add other actions...
    
stage.event_key("right", right_key)
def down_key():
    sprite.move_down(20)
    # add other actions...
    
stage.event_key("down", down_key)
def down_key():
    sprite.move_down(20)
    # add other actions...
    
stage.event_key("down", down_key)
def up_key():
    sprite.move_up(20)
    # add other actions...
    
stage.event_key("up", up_key)

