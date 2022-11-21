import pygame
import json

class Text:
  def __init__(self):
  lines = []
  textfile = open("assets/storytext.json")
  text_dictionary = json.load(textfile)
  self.start = text_dictionary['story']
  
  def add_text(self, start_story):
    self.start = 

  def remove_text(self):
    pass