import pygame
import random

class Item(pygame.sprite.Sprite):
  def __init__(self, xpos, ypos, size = 0):
    '''first line to get in the sprite class init'''
    '''sets item position for x coordinate'''
    '''sets item position for y coordinate'''
    '''sets size of item to size variable'''
    '''loads the image of the player'''
    '''gets a new rectangle covering the entire surface'''
    '''sets speed of player to 1'''
    #just the first line you have to put in the sprite class init
    super().__init__(self)
    #rest of model
    self.xpos = xpos
    self.ypos = ypos
    self.size = size
    #this is required
    self.image = pygame.image.load("assets/item.png")
    self.rect = self.image.get_rect()

#may not be neccesary within the context of our game   
def randomposition(self): 
    '''updates x position of item to a random area on screen'''
    '''updates y position of item to a random area on screen'''
    self.rect.xpos += random.randrange(-self.xpos,self.xpos+1)
    self.rect.ypos += random.randrange(-self.ypos,self.ypos+1)
      