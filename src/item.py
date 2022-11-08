import pygame
import random

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, size = 0):
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
    self.x = x
    self.y = y
    self.size = size
    #this is required
    self.image = pygame.image.load("assets/item.png")
    self.rect = self.image.get_rect()

    
def randomposition(self):
    '''updates x pos of item to a random area on screen'''
    '''updates y pos of item to a random area on screen'''
    self.rect.x += random.randrange(-self.x,self.x+1)
    self.rect.y += random.randrange(-self.y,self.y+1)
      