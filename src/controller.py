import pygame
from src.game import *
from src.menu import *

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