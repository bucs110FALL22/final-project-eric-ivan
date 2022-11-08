import pygame

# like an import for classes instead of modules
class Scene(pygame.sprite.Sprite):
  def __init__(self, bgcolor = None, switch_screen = None, screen_width = 640, screen_height = 480):
    '''first line to get in the sprite class init'''
    '''sets the background color for the scene'''
    '''sets the screen width of the scene'''
    '''sets the screen height of the scene'''
    '''switches screen depending on user choice'''
    '''loads the image of player on the screen'''
    '''gets a new rectangle covering the entire surface'''
    # just the first line you have to put to get in the sprite class init           
    super().__init__(self)
    self.bgcolor = bgcolor
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.switch_screen = switch_screen
    # this is required
    self.image = pygame.image.load("assets/scene.png")
    self.rect = self.image.get_rect()

def draw(self, window):
  '''draws the scene with given parameters'''
  pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50))
    