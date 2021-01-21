import guide
import movement
import descriptions
import text_color
import random
import combat

"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.
Kelvin Ngo
Dennis Gyorgy
"""

def character():
  character_name = input("Enter a name for your adventurer: ")
  character_hp = 10
  return character_name, character_hp


def main():
    """Drive the program."""
    guide.INTRODUCTION()
    guide.CONTROLS()
    DIRECTIONS = movement.MOVE_DIRECTION()
    the_map = movement.BOARD()
    char_name, char_hp = descriptions.character()
    list_of_monsters = descriptions.MONSTERS()
    room_description = descriptions.ROOM_DESCRIPTIONS(char_name)
    y_current = 4
    x_current = 0
    movement.mini_map(the_map)
    mission_complete = False
    while not mission_complete:
      players_move = input(f"{text_color.GREEN_TEXT}What do you do?: {text_color.FINISH_COLOR}")

      if players_move in DIRECTIONS:
        valid_move = movement.validate_move(players_move, y_current, x_current)
        
        if valid_move is True:
          the_map, y_current, x_current = movement.player_moving(char_name, players_move, the_map, y_current, x_current)
          
          if random.randrange(5) == 2:
            battle = combat.fight(list_of_monsters[0], char_hp)
            if battle == "won":
              list_of_monsters.pop(0)
            if battle == "ranaway":
              print(f"{char_name} survived to fight another day.")
            else:
              mission_complete = True

          else:
            char_hp = combat.healing(char_hp)
            room_description = descriptions.ROOM_DESCRIPTIONS(char_name)
            print(room_description)
          
        elif valid_move is False:
          print(
            f"There's no opening and the wall seems impenetrable, perhaps you should take a {text_color.YELLOW_TEXT}different path{text_color.FINISH_COLOR}?"
            )
      
      elif players_move == "check map":
        movement.mini_map(the_map)

      elif players_move == "look around":
        print(room_description)

      elif players_move == "help":
        guide.HELP()

      else:
        print(f"{char_name} lost their train of thought.")


if __name__ == "__main__":
    main()
