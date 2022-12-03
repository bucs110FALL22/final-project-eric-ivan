import pygame
import json

# screen dimensions
DISPLAY_WIDTH, DISPLAY_HEIGHT = 480, 270

class Button(pygame.sprite.Sprite):
    def __init__(self, font, text, pos):
        super().__init__()
        '''creates clickable buttons'''
        self.image = font.render(text, True, 'white')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def get_rect(self):
        '''gets a rectangular surface'''
        return self.rect

#groups the question and answer on screen into a single class
class GameSurface():
    def __init__(self, questionList):
        '''sets font for the game, gets the questionlist, answerlist, and checks the length'''
        '''creates a button for each one listed in json'''
        self.font = pygame.font.Font('assets/8-BIT WONDER.TTF', 10)
        self.questionSurface = self.getQuestion(questionList[0], self.font, 10)
        self.answersList = []
        self.final = False
        if len(questionList) < 2:
            self.final = True
            return
        for i, answer in enumerate(questionList[1].keys()):
            button = Button(self.font, answer, (0, 50 + i * 20))
            self.answersList.append((button, answer))

    def toScreen(self, window):
        '''draws the question and answer on to the screen'''
        window.blit(self.questionSurface, (0, 0))
        for buttonTuple in self.answersList:
            button = buttonTuple[0]
            window.blit(button.image, button.get_rect().topleft)

    def user_response(self, mouse_location):
        '''tracks users click on button, returning button'''
        for button in self.answersList:
            if button[0].get_rect().collidepoint(mouse_location):
                return button[1]

    def getQuestion(self, questionList, font, fontSize):
        '''creates a question surface for each line in questionList'''
        questionSurface = pygame.Surface(
            (DISPLAY_WIDTH, len(questionList) * fontSize))
        for i, text in enumerate(questionList):
            surface = font.render(text, True, 'white')
            questionSurface.blit(surface, (0, i * fontSize))
        return questionSurface

#gameplay class. similar to the menus.
class GamePlay():
    def __init__(self, game):
        '''opens storytext.json file, reads it, and closes it'''
        '''takes the current question and puts it on gamesurface'''
        textfile = open("assets/storytext.json")
        self.text_dictionary = json.load(textfile)
        textfile.close()
        self.option = "1"
        self.currentQuestion = self.text_dictionary[self.option]
        self.gameSurface = GameSurface(self.currentQuestion)
        self.game = game

    def display_menu(self):
        '''displays menu needed to call play'''
        self.play()

    def play(self):
        '''while loop checks if running tracks mouse click position'''
        '''if user clicks displays current question, if choice is = 0 quits game'''
        '''for final user reponse last click ends game'''
        running = True
        while running:
            self.game.window.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_position = pygame.mouse.get_pos()
                    self.response = self.gameSurface.user_response(
                        mouse_position)
                    if self.response:
                        self.option = self.currentQuestion[1][self.response]
                        self.currentQuestion = self.text_dictionary[
                            self.option]
                        if self.currentQuestion == 0:
                            pygame.quit()
                            exit()
                        self.gameSurface = GameSurface(self.currentQuestion)
            self.gameSurface.toScreen(self.game.window)
            pygame.display.update()
            if self.gameSurface.final:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        pygame.quit()
                        exit()

# Menu Class (Controller Class Line 175)
class Menu():
    def __init__(self, game):
        '''references game objects to re-use them'''
        '''save the reference to game, gives access to all variables & functions in game object'''
        '''gets mid width, mid height of screen'''
        '''tells our menu to keep running'''
        '''cursor keeps track of arrows traversing menu'''
        '''offset for cursor so not on top but on left'''
        self.game = game
        self.mid_width, self.mid_height = self.game.DISPLAY_WIDTH / 2, self.game.DISPLAY_HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)  #x, y, width, height
        self.offset = -100  # negative achieves this

    def draw_cursor(self):
        '''draws the cursor'''
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        '''references variables from game object'''
        '''resets the keys'''
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()  # physically moves image to display screen
        self.game.reset_keys()

# Creating Main Menu Class
class MainMenu(Menu):  #putting Menu inherits value from base class
    def __init__(self, game):
        '''uses previous init function'''
        '''cursor points at start game'''
        '''drawing the startx and starty for start game text in middle of screen'''
        '''draws for options state (moves it down by +20)'''
        '''draws for credits state (moves it down by +20)'''
        '''assign a starting position for our cursor'''
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_width, self.mid_height + 30
        self.optionsx, self.optionsy = self.mid_width, self.mid_height + 50
        self.creditsx, self.creditsy = self.mid_width, self.mid_height + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        '''displays the menu with text'''
        '''set true again to make sure its always true when needed'''
        '''in while loop sets flags, checks for user input, draws the titles'''
        '''in while loop we also draw the menu selection texts'''
        '''draws the cursor & blits all of them to the screen'''
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            # draws title: Main Menu (aligns slightly above rest of text)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_WIDTH / 2,
                                self.game.DISPLAY_HEIGHT / 2 - 20)
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
        '''all cursor movement features with states'''
        '''tracks the up or down keys pressed by user to change states'''
        '''checks the states, adjust the cursor, and re-adjust the state'''
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset,
                                           self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset,
                                           self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset,
                                           self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset,
                                           self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset,
                                           self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset,
                                           self.optionsy)
                self.state = 'Options'

    def check_input(self):
        '''check if player wants to move cursor'''
        '''user selects menu (changes menu state)'''
        '''tells current menu to stop displaying'''
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.current_menu = self.game.gameplay
            elif self.state == 'Options':
                self.game.current_menu = self.game.options
            elif self.state == 'Credits':
                self.game.current_menu = self.game.credits
            self.run_display = False

# creates options menu
class OptionsMenu(Menu):
    def __init__(self, game):
        '''pass reference to the game, calls menu base classes' initiator'''
        '''creates option menu'''
        '''navigate through volume & control settings'''
        '''set a starting position for our cursor (aligns volume first, then control settings)'''
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_width, self.mid_height + 20
        self.controlsx, self.controlsy = self.mid_width, self.mid_height + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    # matches same name as old menu
    def display_menu(self):
        '''while loop checks events runs check_inputs() function'''
        '''draws text on the screen and cursor, then blits to screen'''
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_WIDTH / 2,
                                self.game.DISPLAY_HEIGHT / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_inputs(self):
        '''functions checks for user input'''
        '''wants current menu to be set to the main menu'''
        '''ends display_menu loop'''
        '''checks if up or down key have been pressed'''
        '''if state is volume switches to controls'''
        '''if state is controls switches to volume'''
        if self.game.BACK_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset,
                                           self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            pass

# creates credits menu
class CreditsMenu(Menu):
    def __init__(self, game):
        '''pass reference to the game, calls menu base classes' initiator for credit menu'''
        Menu.__init__(self, game)

    def display_menu(self):
        '''displays the credit menu'''
        '''setting display variable = to true'''
        '''inside while loop gathers info from player every frame'''
        '''based on players input sends them back to main menu'''
        '''if start or back key is pressed then goes back to main menu'''
        '''current menu is set to the main menu'''
        '''ends display_menu loop and resetting screen to black'''
        '''draws our text title and credits. '''
        '''blits screen inherited from menu base class'''
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_WIDTH / 2,
                                self.game.DISPLAY_HEIGHT / 2 - 20)
            self.game.draw_text('Made by Eric Pan and Ivan Yun', 15,
                                self.game.DISPLAY_WIDTH / 2,
                                self.game.DISPLAY_HEIGHT / 2 + 10)
            self.blit_screen()

## Controller Class
class Controller():
    def __init__(self):
        '''initiates pygame.init()'''
        '''when game is on, player is playing'''
        '''tracks players actions'''
        '''finds font files, adding the color it'''
        '''references main menu object, creates options menu, and credits menu'''
        '''allows current menu variable to change depending on which menu user wants to select'''
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 480, 270  # canvas dimensions (width, height)
        self.display = pygame.Surface(
            (self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode(
            (self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.font_name = 'assets/8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)  # won't be changing
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.gameplay = GamePlay(self)
        self.current_menu = self.main_menu

    # game loop
    def game_loop(self):
        '''while the player is playing'''
        '''storing possible paths from storytext.json in story_text as a list'''
        story_text = [
            "1",
            "1A",
            "1B",
            "1B.A",
            "1B.B",
            "1B.A.A",
            "1B.A.B",
            "1.B.B",
        ]

    # checking user events
    def check_events(self):
        '''checks user events'''
        '''if event.type = pygame.QUIT stops current menu from running'''
        '''sets user key events to true'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
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
        '''resets the keys and set them to false'''
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        '''draws the text on the screen'''
        '''loads the font'''
        '''creates a rectangular image of our text'''
        '''assigns x, y position to the center of the rectangle'''
        '''pygame takes all necessary stuff & puts it on the screen'''
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()  # x, y, width, height
        text_rect.center = (x, y)  # centers on x, y parameters
        self.display.blit(text_surface, text_rect)