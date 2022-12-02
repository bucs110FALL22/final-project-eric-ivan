import pygame
import json

class Text:
  def __init__(self):
  lines = []
  textfile = open("assets/storytext.json")
  self.text_dictionary = json.loads(textfile)
  print(text_dictionary)
  textfile.close()


