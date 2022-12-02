  # while self.playing:
        #     # check players input events
        #     self.check_events()
        #     # breaks loop but does not turn game off
        #     if self.START_KEY:
        #         self.playing = False
        #     # our canvas
        #     self.display.fill(self.BLACK)
        #     # text, size, x, y
        #     self.draw_text('Thanks for Playing', 20, self.DISPLAY_WIDTH / 2,
        #                    self.DISPLAY_HEIGHT / 2)
        #     # aligns display with window
        #     self.window.blit(self.display, (0, 0))
        #     pygame.display.update()  # physically moves image to display screen
        #     self.reset_keys()

# pygame.init()

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)

# gameDisplay = pygame.display.set_mode((600, 350))

# pygame.display.set_caption('Choose Your Own Adventure')

# pygame.display.update()

# #Images
# background_img = pygame.image.load('background.png')

# #Characters
# class Character(pygame.sprite.Sprite):
#   def __init__(self, type):
#     super().__init__()
#     # self.walk.anim = [
#     #     pygame.image.load(os.path.join("Assets", type, f"{type}_Standing.png"))
      


# gameRunning = True
# lead_x = 300
# lead_y = 300

# while gameRunning:
#   gameDisplay.blit(background_img, (0, 0))
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       gameRunning = False
#   pygame.display.update()

# pygame.quit()
# quit()

# # Other code
# # gameDisplay.fill(WHITE)
# # pygame.draw.rect(gameDisplay, BLACK, [400,300,10,100]) #surface, color, [x,y,width,height]
# # # gameDisplay.fill(red, rect[])