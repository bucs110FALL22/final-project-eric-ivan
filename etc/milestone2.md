# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Scene Interface
***
class Scene:
  def __init__(self, bgcolor = black, switch = None, screen_width = 640, screen_height = 480):
    self.bgcolor = bgcolor
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.switch_screen = switch_screen

***
## Player Interface
***
class Player:
  def __init__(self, xpos = 0, ypos = 1, lives = 3):
    self.xpos = xpos
    self.ypos = ypos
    self.lives = lives

***

## Item Interface
***
class Item:
  def __init__(self, image, xpos = 0, ypos = 0, size = 1):
    self.image = image
    self.xpos = xpos
    self.ypos = ypos
    self.size = size
    
***
========================
