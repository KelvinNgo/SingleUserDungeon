"""contains combat functions"""
import random


def run_away(monster, player_health):
  """Player runs away

  This function allows the player to run away 
    
  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has  
  :return: change the status of player to ranaway   
  """
  n = player_health
  print("You turn away but there is a chance that " + monster[0] +
        " will attack you as you flee")
  if random.random() <= 0.1:
      print(monster[0] + " has attacked!")
      m = roll_dice(4)
      n = n - m
      if n <= 0:
          print("Oh no! You have been vanquished by " + monster[0] +
                  " Game over")
          quit()
      else:
          print("you escaped with some damage")
          y = (n, "ranaway")
          return y
  else:
      print(monster[0] + " has retreated into the shadows")
      m = (n, "ranaway")
      return m


def roll_dice(range):
  """Roll dice once.

  this function simulates a die being rolled once of inputed side length
    
  :param range: the number of sides the die has
  :return: the number roll_dice 
  """
  n = random.randrange(1, range + 1)
  return n


def draw(monster, player_health):
  """Simulate a draw between monster and player.

  This function causes a draw to happen 

  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has 
  :return: whether the player ran away or is in progress
  """
  print("There has been a draw!")
  n = input("Press 'f' to fight or 'r' to run away: ")
  if n == "r":
      return run_away(monster, player_health)
  else:
      return (monster, player_health, "in progress")


def monster_beats_player(monster, player_health):
  """Simulate player receiving damage

  This function causes to player to receive damage 

  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has 
  :return: whether the player ran away or is in progress
  """
  print(monster[0] +
        " has struck you with an arrow! You suffer a damage of 1")
  n = player_health - monster[3]
  print("do you want to fight another round?: ")
  m = input("Enter 'f' to keep fighting or 'r' to run away: ")
  if m == "r":
      return run_away(monster, n)
  else:
      r = (n, "in progress")
      return r


def player_beats_monster(monster, player_health):
  """Simulate player dealing damage.

  This function causes the monster to get damaged

  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has 
  :return: whether the player ran away or is in progress
  """
  print("You hit " + monster[0] + " so hard in the face they suffered " +
        str(monster[4]) + " damage")
  print("Do you want to keep fighting another round?")
  m = input("Enter 'f' to keep fighting or 'r' to run away: ")
  if m == "r":
      return run_away(monster, player_health)
  else:
    return (0, "in progress")


def monster1(monster, player_health):
  """Simulate combat with a monster

  This function starts a fight between a the player and a monster
    
  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has 
  :return: whether the player won or ran away (losing quits the game)
  """
  n = player_health
  monster_health = monster[2]
  print("'Hello! I am " + monster[0] + " the " + monster[1] +
        ". Who dares try to cross my path?'")
  while n >= 0 and monster_health >= 0:
      print("You will both now roll the dice: ")
      player_roll = roll_dice(20)
      monster_roll = roll_dice(20)
      if monster_roll > player_roll:
          p = monster_beats_player(monster, n)
          n = n - monster[3]
          return
          if p[1] == "ranaway":
              return p[1]
      if player_roll > monster_roll:
          p = player_beats_monster(monster, n)
          new_monster_health = monster[2] - monster[4]
          monster_health = new_monster_health
          if p[1] == "ranaway":
              return p[1]
      if monster_roll == player_roll:
          draw(monster, n)
  if n == 0:
      print("Oh no! You have been vanquished by " + monster[0] +
            " Game over")
      quit()
  if monster_health == 0:
      print("congrats! You have defeated " + monster[0])
      y = ("won", n)
      return y


def finalboss(monster, player_health):
  """Simulate fight with final boss.

  This function starts a fight between the player and the Final Boss
    
  :param monster: the final entry from the list of monsters 
  :param player_health: the number of lives the player has 
  :return: whether the player won or ran away (losing quits the game)
  """
  n = player_health
  monster_health = monster[2]
  print(
      "'Hello! I am the Big Dragon the Final Boss!!! You will not get past me *roar*"
  )
  while n >= 0 and monster_health >= 0:
      print("You will both now roll the dice: ")
      player_roll = roll_dice(20)
      monster_roll = roll_dice(20)
      if monster_roll > player_roll:
          p = monster_beats_player(monster, n)
          n = p[1]
          if p[2] == "ranaway":
              return
      if player_roll > monster_roll:
          p = player_beats_monster(monster, n)
          monster1 = p[0]
          new_monster_health = monster1[2]
          monster_health = new_monster_health
          if p[2] == "ranaway":
              return
      if monster_roll == player_roll:
          draw(monster, n)
  if n == 0:
      print("Oh no! The Dragon vanquished you...")
      quit()
  if monster_health == 0:
      print("congrats! You have defeated the Dragon!")
      y = ("won", n)
      return y


def fight(monster, player_health):
  """Start fight between player and monster.

  This function starts a fight and returns whether the player won or ran away
   
  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has 
  :return: whether the player won or ran run_away
  """
  if monster[0] == "Dragon":
      finalboss(monster, player_health)
  else:
      n = monster1(monster, player_health)
      return n


def combat(monster, player_health):
  """Start a round of combat.

  This function starts a round of combat for the player

  :param monster: a single tupple consisting of info about the monster
  :param player_health: the number of lives the player has 
  :return: whether a player won the fight or ran away as well as their new health

  >>> combat(("Bazilisk", "A long snake with piercing eyes", 3, 2, 1), 9)

  """
  print(monster[1] + "appears before you!")
  n = input(
      "Would you like to run away or fight? (press the 'r' key to run away or the 'f' key to fight) : "
    )
  if n == "r":
      print("You have chose to run from: " + monster[0])
      run_away(monster, player_health)
  else:
      print("You have chosen to fight!")
      n = fight(monster, player_health)
      m = player_health
      if n[0] == "won":
          return "won", m
      else:
          return "ranaway", m


def healing(character_hp):
  """Simulate player recovering health points
  
  :param character_hp: current hp of character_hp
  :return: updated hp of character
  """
  if 10 > character_hp:
    character_hp += 2
    return character_hp

  elif character_hp == 9:
      character_hp = 10
      return character_hp

  else:
      return character_hp
