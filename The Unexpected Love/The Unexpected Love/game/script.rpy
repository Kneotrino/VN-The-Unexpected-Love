# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# # init python:
    
#     show_window_trans = MoveTransition(0.25,
#                                        enter_factory=MoveIn((None, 
#                                        1.0, None, 0.0)))

#     hide_window_trans = MoveTransition(0.25,
#                                        leave_factory=MoveOut((None, 
#                                        1.0, None, 0.0)))
        
#     def hide_window():
#         store._window_during_transitions = False
#         narrator("", interact=False)
#         renpy.with_statement(None)
#         renpy.with_statement(hide_window_trans)

#     def show_window():
#         narrator("", interact=False)
#         renpy.with_statement(show_window_trans)
#         store._window_during_transitions = True




# Init some variable
init:

    # Set up the size of the screen, and the window title.
    $ config.screen_width = 1280
    $ config.screen_height = 720

    # Set this to true to enable some developer-specific
    # functionality. It should be false in a finished game.
    # Read the "Developer Tools" section of the reference
    # to see what this enables.
    $ config.developer = True

    # Declare the images that are used in the program.

    # Backgrounds.
    # image bg paulin_bedroom = "res/bg/paulin_bedroom.jpg"
    image black = Solid((0, 0, 0, 255))

    # Image Location
    $ screen_center = Position(xpos=0.5, ypos=0.5)

    # Charater
    $ letter = Character(None, kind=nvl)
    $ Paulin = Character("Paulin")

# The game starts here.

label start:

    window show dissolve
    image book_cover = "res/img/book_cover.png"
    show book_cover at screen_center with dissolve

    "based on The Unexpected Love by LittleWhiteCloud"

    jump prolog