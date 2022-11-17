import pygame
from game import Game
g = Game()

while g.running:
  g.current_menu.display_menu()
  # if player presses start & display menu functions, playing variable set to true, enters game loop
  g.game_loop()

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

gameDisplay = pygame.display.set_mode((600, 350))

pygame.display.set_caption('Choose Your Own Adventure')

pygame.display.update()

#Images
background_img = pygame.image.load('background.png')

#Characters
class Character(pygame.sprite.Sprite):
  def __init__(self, type):
    super().__init__()
    self.walk.anim = [
        pygame.image.load(os.path.join("Assets", type, f"{type}_Standing.png"))
      ]


gameRunning = True
lead_x = 300
lead_y = 300

while gameRunning:
  gameDisplay.blit(background_img, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameRunning = False
  pygame.display.update()

pygame.quit()
quit()

# Other code
# gameDisplay.fill(WHITE)
# pygame.draw.rect(gameDisplay, BLACK, [400,300,10,100]) #surface, color, [x,y,width,height]
# # gameDisplay.fill(red, rect[])