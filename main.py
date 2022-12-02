
import pygame
from src.controller import Controller

def main():
    c = Controller()
  
    while c.running:
      c.current_menu.display_menu()
    # if player presses start & display menu functions, playing variable set to true, enters game loop
      c.game_loop()
main()