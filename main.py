
import pygame
from src.controller import Controller

def main():
    '''c variable is set to controller'''
    '''while controller is running current menu is displayed'''
    '''if player presses start & display menu functions, playing variable set to true, enters game loop'''
    c = Controller()
    while c.running:
      c.current_menu.display_menu()
      c.game_loop()
main()