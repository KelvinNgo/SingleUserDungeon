import text_color
import random

"""Contains your character and names/descriptions used in this game."""


def character():
  """Create a character with name and default hp.

  :return: character name and hp
  """
  character_name = input("Enter a name for your adventurer: ")
  character_hp = 10
  return character_name, character_hp


def MONSTERS():
  """A list of monsters inside dungeon.

  :return: list_of_monster
  """
  list_of_monster = [
  ("Elfy the Elf", "A small elvin creature with a bow and arrows around its back.", 2, 1, 1),
  ("Bazilisk", "A long snake with piercing eyes", 3, 2, 1), 
  ("Shrak the Ogre", "A large green ogre with a penchant for eating people", 4, 2, 2),
  ("Wanda the Witch", "A tall scary looking witch riding a broom", 6, 3, 2),
  ("Dragon", "A large red dragon with the ability to breathe fire", 8, 4, 2)]
  return list_of_monster


def ROOM_DESCRIPTIONS(adventurer):
  """Choose a random room in dungeon.

  :param adventurer: name of the adventurer/player character
  :return: a description of the room with adventurer name filled in for dialogue
  """
  rooms = (
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} is inside a wine cellar, most of it is filled with cracked, empty bottles.\n"
    "Perhaps it is better to not go looking for an intact bottle.\n"
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} suspects it will be very detrimental to their health to fight monsters while drunk.",
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} is inside a gaol, the cells are mostly filled with the skeletons of prisoners long dead.\n"
    "Most of the cell doors are open with the exception of one in the far corner.\n"
    "There seems to be a person in there but they are crouched in the corner muttering to themself.\n"
    "The cleaver they are holding looks very dangerous so perhaps it is best to leave them alone.\n",
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR}is inside a dusty old library, piles and piles of books are scattered amongst the dirty floor.\n"
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} remembers the last time they perused books inside of that nast vampire\'s castle.\n"
    f"The tentacles that came out of the pages almost strangled {text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR}.\n"
    f"Perhaps it is better to finish what {text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} came here to do instead of doing some light reading.",
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} is inside what appears to be a ritual room.\n"
    "The only things inside a room are black candles mounted on the walls and a pentagram in the middle of the floor.\n"
    f"The pentagram appears to be made from dried blood, {text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} would rather not think of who or what provided that blood.\n"
    "On each corner of the star there appears to be a random assortment of objects.\n"
    "For some reason one of them looks like a phallic object.\n"
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} decides they don\'t want to stay here any longer than they have to.",
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} is inside their childhood bedroom.\n"
    f"The bed and drawer is just like how they remember it.\n"
    f"There's even that empty aquarium {adventurer} left inside their room even though the fish all died within a day.\n"
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} would rather not think too hard about why their room is inside of a dungeon.\n",
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} is inside of a sewer, the smell feels like its burning away their nostril hairs.\n"
    f"{text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} wonders how there could even be a sewer when the doors connecting it lead into different rooms.\n"
    f"As {text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} stands there they see a figure in their peripheral vision.\n"
    "What looks like a large bipedal rat is standing there 4 smaller bipedal turtles.\n"
    f"Before {text_color.MAGENTA_TEXT}{adventurer}{text_color.FINISH_COLOR} can say anything a large cloud of smoke appears and when it disappears they are gone.\n"
    )
  return random.choice(rooms)
