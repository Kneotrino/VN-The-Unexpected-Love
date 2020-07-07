# The script of the game goes in this file.

# TODO
# add bgm

# Declare the characters.

init python:

    # A list of section and tutorial objects.
    tutorials = [ ]

    class Section(object):
        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        """
        Represents a label that we can jump to.
        """

        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            tutorials.append(self)


    Section(_("Content"))

    Tutorial("prolog", _("Prolog"))

    # Tutorial("Label", _("Chapter Name"))
    Section(_("Chapters 1-10"))
    Tutorial("chapter1", _("Chapter 1"))
    Tutorial("chapter2", _("Chapter 2"))
    Tutorial("chapter3", _("Chapter 3"))
    # Tutorial("chapter4", _("Chapter 4"))
    # Tutorial("chapter5", _("Chapter 5"))
    # Tutorial("chapter6", _("Chapter 6"))
    # Tutorial("chapter7", _("Chapter 7"))
    # Tutorial("chapter8", _("Chapter 8"))
    # Tutorial("chapter9", _("Chapter 9"))
    # Tutorial("chapter10", _("Chapter 10"))

    # Section(_("Chapters 11-20"))
    # Tutorial("chapter11", _("Chapter 11"))
    # Tutorial("chapter12", _("Chapter 12"))
    # Tutorial("chapter13", _("Chapter 13"))
    # Tutorial("chapter14", _("Chapter 14"))
    # Tutorial("chapter15", _("Chapter 15"))
    # Tutorial("chapter16", _("Chapter 16"))
    # Tutorial("chapter17", _("Chapter 17"))
    # Tutorial("chapter18", _("Chapter 18"))
    # Tutorial("chapter19", _("Chapter 19"))
    # Tutorial("chapter20", _("Chapter 20"))


screen Chapter_Menu(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 120

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt "":
                            size 50
                        null height 5

        bar adjustment adj style "vscrollbar"

        textbutton _("Kembali ke Menu Utama"):
            xfill True
            action Return(False)
            top_margin 10



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
    image white = Solid((0, 0, 0, 255))

    # Image Location
    # $ screen_center = Position(xpos=0.5, ypos=0.5)

    # Charater
    $ letter = Character(None, kind=nvl)
    $ Paulin = Character("Paulin")

# The game starts here.

# This is used to preserve the state of the scrollbar on the selection
# screen.
default tutorials_adjustment = ui.adjustment()


label start:

    image bg introduction = "res/bg/choice.png"
    scene bg introduction

    image book_cover = "res/img/book_cover.png"
    show book_cover at Position(xpos=0.5, ypos=0.65)

    "based on The Unexpected Love by LittleWhiteCloud"

    $ renpy.choice_for_skipping()

    call screen Chapter_Menu(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    call expression tutorial.label from _call_expression

label end:
    return
