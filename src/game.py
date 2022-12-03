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