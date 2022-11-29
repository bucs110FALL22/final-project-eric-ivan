timport pygame
import random

# like an import for classes instead of modules
class Player(pygame.sprite.Sprite):
  def __init__ (self):
    '''first line to get in the sprite class init'''
    '''health of player set to 3'''
    '''player directon set to 3'''
    '''loads the image of the player'''
    '''player lives set to 3'''
    '''gets a new rectangle covering the entire surface'''
    '''sets speed of player to 1'''
    # just the first line you have to put to get in the sprite class init           
    super().__init__(self)
    # rest of model
    self.lives = 3
    self.direction = 3
    # this is required
    self.image = pygame.image.load("assets/player.png")
    self.rect = self.image.get_rect()
    self.speed = 1
    
    # def move(self, direction):

    def move_up(self):
      '''player moving upwards'''
      self.rect.y -= self.speed
      
    def move_down(self):
      '''player moving downwards'''
      self.rect.y += self.speed
      
    def move_right(self):
      '''player moving to the right'''
      self.rect.x += self.speed
      
    def move_left(self):
      '''player moving to the left'''
      self.rect.x -= self.speed
  