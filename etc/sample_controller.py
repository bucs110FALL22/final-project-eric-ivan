import pygame
import random

class Controller:
  
  def __init__(self):
    '''initializing pygame features'''
    '''creating a display surface'''
    '''setting the background color'''
    pygame.init() #setup pygame data
    self.screen = pygame.display.set_mode()
    self.background = "Black"
    '''generating a random number of items'''
    '''getting the window width & height'''
    '''changing the width of window depending on # of items'''
    number_of_items = random.randint(0,10) # generates a random number of items 1, 10
    size = pygame.display.get_window_size() # width and height
    width = size[0] / number_of_items #changes width depending on # of items
    self.screen = pygame.display.set_mode(size[0],width)
    '''default scene 1 in the background of game'''
    '''default scene 2 in the background of game'''
    '''default scene 3 in the background of game'''
    '''layout of the main menu background / interface'''
    '''if a user loses then it displays gameover default screen'''
    self.scene1
    self.scene2
    self.scene3
    self.mainmenu
    self.gameoverscreen
  
  def mainloop(self):
    '''keep the gaming running if its true'''
    '''starting while loop for running = True'''
    '''if user decides to close the event window (see below)'''
    '''if event type equals false running = False so loop stops'''
    '''if statement for players y position < 0 (checks for boundaries)'''
    '''if y position is < 0 (outside of screen) then player bounces downward'''
    '''if y position is > 0 (outside of screen) then player bounces upward'''
    '''if staement for when players life is > 0'''
    '''if player somehow collides with death (a certain choice causes this)'''
    '''then subtracts 1 life from the player'''
    '''else if player doesn't collide with death then'''
    '''then the player is kept alive'''
    '''and the player can still move'''
    '''updates the display depending on the loop'''
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
      if self.player.y < 0: 
        self.player.direction = "down" # make it so it bounces the player back
      elif self.player.y > self.height: 
        self.player.direction = "up" # make it so it bounces the player back
      while self.player.life > 0:
        if self.player.rect.collidepoint(self.death):
          self.player.life -= 1
        else:
          self.play.keepalive = True
          self.player.direction = True 
    #select state loop
    pygame.display.update()
  ### below are some sample loop states ###

  def menuloop(self):
    '''if the screen is equal to main menu'''
    '''then make a function with main menu components'''
    '''play buttons function with other options'''
    '''while the loop is true get mouse position'''
    '''set and fill the background color'''
    '''blit the text a sort of start message '''
    '''generates back button with parameters'''
    '''pygame event loop so if use quits goes back to main menu'''
    '''updates screen data depending on user choice'''
    '''updates the pygame display'''
    #event loop
    while self.screen == self.mainmenu:
      def mainmenu():
        '''includes main menu components'''
      def play():
        pygame.display.set_caption("Play")

        while True:
          self.mouse.pos = pygame.mouse.get_pos()
          self.screen.fill("black")

          self.text = "Start message"
          self.screen.blit(self.text)

          self.back = self.backbutton(image = None, pos = (self.x,self.y), text = "Back", font = None, color = None)
          
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              pygame.system.exit()
            if event.type == pygame.MOUSEBUTTONDOW:
              if self.back.checkForInput(self.mouse.pos):
                self.mainmenu()
      #update data
      self.screen = self.screen.update()
      #redraw
      pygame.display.update()
      
  def gameloop(self):
      #event loop
    if self.lives == 0:
      self.STATE = "gameover"
      #update data

      #redraw
      pygame.display.update()
    
  def gameoverloop(self):
      #event loop
    
      #update data
      self.gameovermsg = pygame.msg("Game Over")
      #redraw
      pygame.display.update()
