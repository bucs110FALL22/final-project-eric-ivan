import pygame
import json
# from menu import *

class GameSurface():
  def __init__(self,questionList):
    self.font = pygame.font.Font()# pass in font file here
    self.questionSurface = self.font.render(questionList[0])
    self.answersList = []
    if len(questionList) < 2:
      return
    for answer in questionList[1]:
      button = self.font.render(answer)
      self.answersList.append((button,answer))

  def toScreen(self,window):
    window.blit(self.questionSurface,(0,0))
    for i in len(self.answersList):
      window.blit(self.answersList[i],(0,100+i*20))

  def user_response(self,mouse_location):
    for button in self.answersList:
      if button[0].get_rect().collidepoint(mouse_location):
        return button[1]

class GamePlay():
  def __init__(self):
    textfile = open("assets/storytext.json")
    self.text_dictionary = json.loads(textfile)
    textfile.close()
    self.option = "1"
    self.currentQuestion = self.text_dictionary[self.option]
    self.gameSurface = GameSurface(self.currentQuestion)
  def play(self):
    while True:
      for event in pygame.event.get():
        #if user clicks here
        mouse_position = pygame.mouse.get_pos()
        self.response = self.gameSurface.user_response(mouse_position)
        if self.response:
          self.option = self.currentQuestion[1][self.response]
          self.gameSurface = GameSurface(self.text_dictionary[self.option])
  

# Menu Class (Controller Class Line 175)
class Menu():
    # references game objects to re-use them
    def __init__(self, game):
        # save the reference to game, gives access to all variables & functions in game object
        self.game = game
        # gets mid width, mid height of screen
        self.mid_width, self.mid_height = self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2
        # tells our menu to keep running
        self.run_display = True
        # cursor keeps track of arrows traversing menu
        self.cursor_rect = pygame.Rect(0, 0, 20, 20) #x, y, width, height
        # offset for cursor so not on top but on left
        self.offset = - 100 # negative achieves this
   # draws the cursor
    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    # references variables from game object
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()  # physically moves image to display screen
        self.game.reset_keys()

# Creating Main Menu Class
class MainMenu(Menu): #putting Menu inherits value from base class
    def __init__(self, game):
        Menu.__init__(self, game) # uses previous init function
        self.state = "Start" # cursor points at start game
        # drawing the startx and start y for start game text in middle of screen
        self.startx, self.starty = self.mid_width, self.mid_height + 30
        # draws for options state (moves it down by +20)
        self.optionsx, self.optionsy = self.mid_width, self.mid_height + 50
        # draws for credits state (moves it down by +20)
        self.creditsx, self.creditsy = self.mid_width, self.mid_height + 70
        # assign a starting position for our cursor
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    # display the menu with text
    def display_menu(self):
        # set true again to make sure its always true when needed
        self.run_display = True
        while self.run_display:
            # set all our flags for us
            self.game.check_events()
            # checks for user inputs
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # draws title: Main Menu (aligns slightly above rest of text)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 20)
            # draws Start Game text startx & starty positions
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            # draws Options text with startx & starty positions
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            # draws Credits text startx & starty positions
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    # all cursor movement features
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            # Checks the states, adjust the cursor, and re-adjust the state
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        # check if player wants to move cursor
        self.move_cursor()
        # user selects menu (changes menu state)
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.current_menu = self.game.options
            elif self.state == 'Credits':
                self.game.current_menu = self.game.credits
            # tells current menu to stop displaying
            self.run_display = False

# creates options menu
class OptionsMenu(Menu):
    # pass reference to the game, calls menu base classes' initiator
    def __init__(self, game):
        # navigate through volume & control settings
        Menu.__init__(self,game)
        self.state = 'Volume'
        # tells us where to put volume text
        self.volx, self.voly = self.mid_width, self.mid_height + 20
        self.controlsx, self.controlsy = self.mid_width, self.mid_height + 40
        # set a starting position for our cursor (aligns volume first, then control settings)
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    # matches same name as old menu
    def display_menu(self):
        # setting variable to true
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            # run this functions for what to do with it
            self.check_inputs()
            self.game.display.fill((0, 0, 0))
            # draws text
            self.game.draw_text('Options', 20, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_inputs(self):
        if self.game.BACK_KEY:
            # want current menu to be set to the main menu
            self.game.current_menu = self.game.main_menu
            # ends display_menu loop
            self.run_display = False
        # checks if up or down key have been pressed
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            # if state volume switches to controls
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            # if state controls switches to volume
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

# creates credits menu
class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        # setting display variable = to true
        self.run_display = True
        # inside while loop gathers info from player every frame
        while self.run_display:
            # based on players input sends them back to main  menu
            self.game.check_events()
            # if start or back key is pressed then goes back to main menu
            if self.game.START_KEY or self.game.BACK_KEY:
                # want current menu to be set to the main menu
                self.game.current_menu = self.game.main_menu
                # ends display_menu loop
                self.run_display = False
            # resetting screen to black
            self.game.display.fill(self.game.BLACK)
            # draw our text title and credits
            self.game.draw_text('Credits', 20, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 - 20)
            self.game.draw_text('Made by Eric Pan and Ivan Yun', 15, self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2 + 10)
            self.blit_screen() #inherited from menu base class

## Controller Class
class Controller():
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
        # a way for referencing main menu object
        self.main_menu = MainMenu(self) # won't be changing
        # creates options menu
        self.options = OptionsMenu(self)
        # creates credits menu
        self.credits = CreditsMenu(self)
        # allows current menu variable to change depending on which menu user wants to select
        self.current_menu = self.main_menu

    # game loop
    def game_loop(self):
        # while player is playing
      story_text = ["1", "1A", "1B", "1B.A", "1B.B", "1B.A.A", "1B.A.B", "1.B.B", ]
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
                # stops current menu running to stop
                self.current_menu.run_display = False
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
