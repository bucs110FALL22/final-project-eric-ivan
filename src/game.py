import pygame

class Game():
  def __init__(self):
    pygame.init()
    # game is on, player is playing
    self.running, self.playing = True, False
    # tracks players actions
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 480, 270  # canvas dimensions (width, height)
    self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
    self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
    # finding font files
    self.font_name = '8-BIT WONDER.TTF'
    # default: font = pygame.font.get_default_font()
    # adding the color
    self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

  # game loop
  def game_loop(self):
    # while player is playing
    while self.playing:
      # check players input events
      self.check_events()
      # breaks loop but does not turn game off
      if self.START_KEY:
          self.playing = False
      # our canvas
      self.display.fill(self.BLACK)
      # text, size, x, y
      self.draw_text('Thanks for Playing', 20, self.DISPLAY_WIDTH/2, self.DISPLAY_HEIGHT/2)
      # aligns display with window
      self.window.blit(self.display, (0, 0))
      pygame.display.update()  # physically moves image to display screen
      self.reset_keys()


  # checking user events
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running, self.playing = False, False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            self.START_KEY = True
        if event.key == pygame.K_BACKSPACE:
            self.BACK_KEY = True
        if event.key == pygame.K_DOWN:
            self.DOWN_KEY = True
        if event.key == pygame.K_UP:
            self.UP_KEY = True

# sets key to false
  def reset_keys(self):
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

  # draws text on dscreen
  def draw_text(self, text, size, x, y):
    # loadng font
    font = pygame.font.Font(self.font_name, size)
    # created a rectangular image of our text
    text_surface = font.render(text, True, self.WHITE)
    text_rect = text_surface.get_rect() # x, y, width, height
    # assigns x, y position to the center of the rectangle
    text_rect.center = (x,y) # centers on x, y parameters
    # pygame takes all necessary and puts it on the screen
    self.display.blit(text_surface, text_rect)
