import doctest
import text_color

"""Contains movement functions"""


def BOARD():
  """Create a nested list to represent the map.

  :return: A nested list
  
  >>> BOARD()
  [["x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x"],
  [f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x", "x", "x", "x"]]
  """
  board_map = [["x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x"], ["x", "x", "x", "x", "x"],
               [f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x", "x", "x", "x"]]
  return board_map


def mini_map(dungeon):
  """Turn a nested list into a grid to represent map.
  
  :param dungeon: a nested list
  :return: prints out a grid

  >>> test_dungeon = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
  >>> mini_map(test_dungeon)
  x x x
  x x x
  x x x
  """
  for lists in dungeon:
    print(" ".join(map(str, lists)))



def player_direction(adventurer, direction, y_axis, x_axis):
  """Simulate movement movement of character along y and x-coordinates.

  :param direction: represents moving in a cardinal direction
  :param y_axis: represents the y coordinate
  :param x_axis: represents the x x_coordinate
  :return: rew coordinates after moving in a direction

  >>> player_direction("ron", "move north", 1, 1)
  ron moves north...
  (0, 1)
  >>> name = "ron"
  >>> player_direction("ron", "move south", 1, 1)
  ron moves south...
  (2, 1)
  >>> player_direction("ron", "move east", 1, 1)
  ron moves east...
  (1, 2)
  >>> player_direction("ron", "move west", 1, 1)
  ron moves west...
  (1, 0)
  """
  if direction == "move north":
    y_axis -= 1
    direction = "moves north"
  
  elif direction == "move south":
    y_axis += 1
    direction = "moves south"

  elif direction == "move east":
    x_axis += 1
    direction = "moves east"

  elif direction == "move west":
    x_axis -= 1
    direction = "moves west"

  print(f"{adventurer} {text_color.BLUE_TEXT}{direction}{text_color.FINISH_COLOR}...")
  return y_axis, x_axis


def player_location(location, old_y, old_x, new_y, new_x):
  """Mark new location of player in index and unmark old location
  
  :param location: a nested list
  :param old_y: current outer index
  :param old_x: current inner index
  :param new_y: new outer index
  :param new_x: new inner index
  :return: nested list with a new marker for current location

  >>> test_y = [[f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x"]]
  >>> player_location(test_y, 0, 0, 1, 0)
  ([["x", "x"], [f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"]], 1, 0)
  >>> test_x = [[f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x"]]
  >>> player_location(text_x, 0, 0, 0, 1)
  ([["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}"], ["x", "x"]], 0, 1)
  """
  location[new_y][new_x] = f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}"
  location[old_y][old_x] = "x"
  return location, new_y, new_x


def player_moving(adventurer, path, current_location, y_coord, x_coord):
  """Change the index location of player depending on cardinal direction of their move.
  
  :param path: cardinal direction
  :param current_location: a nested list with an indicator for current location
  :param y_coord: represents current y-coordinate
  :param x_coord: represents current x-coordinate
  :return: a nested list with the indicator having moved in cardinal direction

  >>> test_north = [["x", "x", "x"], ["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x", "x"]]
  >>> player_moving("move north", test_north, 1, 1)
  ([["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x", "x"], ["x", "x", "x"]], 0, 1)
  >>> test_south = [["x", "x", "x"], ["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x", "x"]]
  >>> player_moving("move south", test_south, 1 ,1)
  ([["x", "x", "x"], ["x", "x", "x"], ["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"]], 2, 1)
  >>> test_east = [["x", "x", "x"], ["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x", "x"]]
  >>> player_moving("move east", test_east, 1, 1)
  ([["x", "x", "x"], ["x", "x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}"], ["x", "x", "x"]], 1, 2)
  >>> test_west = [["x", "x", "x"], ["x", f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x"], ["x", "x", "x"]]
  >>> player_moving("move west", test_west, 1, 1)
  ([["x", "x", "x"], [f"{text_color.CYAN_TEXT}#{text_color.FINISH_COLOR}", "x", "x"], ["x", "x", "x"]], 1, 0)

  """
  new_y, new_x = player_direction(adventurer, path, y_coord, x_coord)
  current_location, y_current, x_current = player_location(current_location, y_coord, x_coord, new_y, new_x)
  mini_map(current_location)
  return current_location, y_current, x_current



def validate_move(direction, check_y, check_x):
  """Determine if your move will take you beyond the boundary.

  :param direction: the cardinal direction of your movement
  :param check_y: current y-coordinate
  :param check_x: current x-coordinate
  :return: True or False depending on if move will take you outside boundary

  >>> validate_move("move north", 1, 1)
  True
  >>> validate_move("move north", 0, 1)
  False
  >>> validate_move("move south", 3, 1)
  True
  >>> validate_move("move south", 4, 1)
  False
  >>> validate_move("move east", 1, 3)
  True
  >>> validate_move("move east", 1, 4)
  False
  >>> validate_move("move west", 1, 1)
  True
  >>> validate_move("move west", 1, 0)
  False
"""
  if direction == "move north":
    if 0 > check_y - 1:
      return False
    else:
      return True

  elif direction == "move south":
    if check_y + 1 > 4:
      return False
    else:
      return True

  elif direction == "move east":
    if check_x + 1 > 4:
      return False
    else:
      return True

  elif direction == "move west":
    if 0 > check_x - 1:
      return False
    else:
      return True


def MOVE_DIRECTION():
  return ("move north", "move south", "move east", "move west")


if __name__ == '__main__':
  doctest.testmod()
