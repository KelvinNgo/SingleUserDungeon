"""Contains functions for the intro and help guide"""


def INTRODUCTION():
  """Print introduction to the game."""
  print("Welcome to PLACEHOLDERNAME, in this game you run around a dungeon and slay monsters.\n"
  "Your current location is represented by #.\n"
  "Whenever you move to a new room, there is a 1 in 4 chance of encountering a monster!\n"
  "You start at 10 HP and moving to a new room will heal you for 2 HP unless you enter combat, never exceeding 10 HP.\n"
  "If you die, the game will end.\n"
  "Otherwise, to beat the game you must find and slay every monster in the dungeon.\n"
  "Then you will fight the boss.\n"
  "Good luck adventurer!\n"
  )


def CONTROLS():
  """Print gontrols of the game."""
  print("The controls of this game are simple, but you must be precise!\n"
  "To start, every command you enter must be in lowercase otherwise nothing will happen.\n"
  "To traverse the dungeon, the command is \"move <direction>\" and you can go north, south, east, or west.\n"
  "Before you enter combat, you can choose to fight or flee.\n"
  "To fight, enter \"fight\", otherwise to flee the command is \"flee\".\n"
  "When you enter combat, you will automatically fight the monster until you win or perish.\n"
  "To check your current location again, enter \"check map\".\n"
  "To check your surroundings again, enter \"look around \".\n"
  "If you forget the controls, enter \"help\" to see these guide again.\n"
  )


def HELP():
  """Print the controls again."""
  CONTROLS()