import random
import time
import math


class Player:

  def __init__(self, name, memory):
    self.name = name
    self.memory = memory


players = []
elimedPlayers = []
juryClick = 0
longestNameLength = 0
jurors = []
playercount = 0


def AddingPlayers():
  print(
    "Enter the player's name. Type 'Done' when you're done entering names.")
  x = input()
  while (x.lower() != 'done'):
    global playercount
    global longestNameLength
    longestNameLength = max(longestNameLength, len(x))
    playercount += 1
    players.append(Player(x, []))
    x = input()
  global juryClick
  juryClick = math.ceil(playercount / 2)
  if (juryClick % 2 == 0):
    juryClick += 1


def Cycle():
  eligible = []
  global playercount
  global juryClick
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  #Announce living people

  if (playercount == juryClick):
    print("With there being", playercount,
          "players remaining, the Jury phase has started.")
    time.sleep(1.5)

  print(playercount, "players left:")
  for x in players:
    eligible.append(x)
    print(x.name)

  time.sleep(1)
  #COALITION PHASE
  print("\n\n\n")

  batshitinsane = random.randint(1, 4)
  if (batshitinsane == 1):
    factionSizeArray = []
    for i in range(2, playercount-4):
      for j in range(0, math.floor(playercount - 1 / i)):
        factionSizeArray.append(i)

    factionSize = factionSizeArray[random.randint(0, len(factionSizeArray) - 1)]
    factionNum = math.floor((playercount - 1) / factionSize)
  else:
    factionSize = random.randint(2, max(min(5,playercount-1), playercount/5))
    factionNum = math.floor((playercount - 1) / factionSize)
  print("You must create \n\n[", factionNum, "] factions of [", factionSize,
        "]\n\n\n")

  overloadPossible = 0
  if (playercount == (factionNum + 1) * factionSize):
    overloadPossible = 1

  time.sleep(1)
  for i in range(factionNum + overloadPossible):
    time.sleep(1.5)
    flopChance = random.randint(1, factionNum)
    if (flopChance <= factionNum + 1 - i + overloadPossible):
      print("A faction has been made!")
      time.sleep(1)
      print("It consists of:")
      for j in range(factionSize):
        time.sleep(1)
        index = random.randint(0, len(eligible) - 1)
        players[players.index(
          eligible[index])].memory.append(" " + str(i + 1) + "  ")
        print(i+1, "-", eligible[index].name)
        eligible.pop(index)
      print("\n")
    else:
      break

  time.sleep(2)
  #RIOT PHASE
  print("\n\n\n")

  riotPlayers = []

  if (len(eligible) == 0):
    print("OVERLOAD!!!")
    time.sleep(1)
    print("All players must participate in the Riot")
    time.sleep(1)
    for x in players:
      riotPlayers.append(x)
      x.memory.pop()
      x.memory.append("RIOT")
  else:
    print("The following players must participate in the Riot")
    for x in eligible:
      time.sleep(1)
      print(x.name)
      riotPlayers.append(x)
      x.memory.append("RIOT")

  if (len(riotPlayers) == 1):
    time.sleep(1)
    print(
      "As there is only 1 player eligible for the Riot, they're instantly eliminated."
    )
    if (playercount <= juryClick):
      jurors.append(riotPlayers[0])
    elimedPlayers.append(riotPlayers[0])
    players.remove(riotPlayers[0])
  else:
    loser = random.randint(0, len(riotPlayers) - 1)
    time.sleep(1)
    print("The player eliminated in the Riot is:")
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print(riotPlayers[loser].name)
    time.sleep(1)
    players[players.index(riotPlayers[loser])].memory.pop()
    players[players.index(riotPlayers[loser])].memory.append("ELIM")
    if (playercount <= juryClick):
      jurors.append(riotPlayers[loser])
    elimedPlayers.append(riotPlayers[loser])
    players.remove(riotPlayers[loser])

  time.sleep(2)
  playercount -= 1


def Finale():
  global playercount
  global juryClick
  for i in range(2):  #F4 and F3
    eligible = []
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if (playercount == juryClick):
      print("With there being", playercount,
            "players remaining, the Jury phase has started.")
      time.sleep(1.5)
    print(playercount, "players left:")
    for x in players:
      x.memory.append("SAFE")
      eligible.append(x)
      print(x.name)

    print("\n\n\n")
    time.sleep(1)
    riotPlayers = []
    for x in eligible:
      time.sleep(1)
      index = random.randint(0, len(eligible) - 1)
      while (eligible[index] == x):
        index = random.randint(0, len(eligible) - 1)
      print(x.name, "nominates", players[index].name, "to the Riot")
      if eligible[index] in riotPlayers:
        continue
      else:
        riotPlayers.append(eligible[index])
        players[players.index(eligible[index])].memory.pop()
        players[players.index(eligible[index])].memory.append("RIOT")

    time.sleep(1)
    print("\n\n\n")
    print("The following players must participate in the Riot:")
    for x in riotPlayers:
      time.sleep(1)
      print(x.name)

    loser = random.randint(0, len(riotPlayers) - 1)
    time.sleep(1)
    print("The player eliminated in the Riot is:")
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print(riotPlayers[loser].name)
    players[players.index(riotPlayers[loser])].memory.pop()
    players[players.index(riotPlayers[loser])].memory.append("ELIM")
    time.sleep(1)
    if (playercount <= juryClick):
      jurors.append(riotPlayers[loser])
    elimedPlayers.append(riotPlayers[loser])
    players.remove(riotPlayers[loser])
    playercount -= 1
    time.sleep(2)

  #F2
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  votes = [0, 0]
  for x in jurors:
    time.sleep(1)
    vote = random.randint(0, 1)
    print(x.name, "has voted for", players[vote].name)
    votes[vote] += 1

  time.sleep(1.5)
  print("With a vote count of", votes[0], "to", votes[1])
  time.sleep(2)
  if (votes[0] > votes[1]):
    print(players[0].name, "has won Eradication!")
    players[0].memory.append("WIN")
    players[1].memory.append("LOSE")
    elimedPlayers.append(players[1])
    elimedPlayers.append(players[0])
  if (votes[1] > votes[0]):
    print(players[1].name, "has won Eradication!")
    players[0].memory.append("LOSE")
    players[1].memory.append("WIN")
    elimedPlayers.append(players[0])
    elimedPlayers.append(players[1])


def MemoryShit():
  time.sleep(1)
  elimedPlayers.reverse()
  jurors.reverse()
  print("\n\n\n")
  for x in elimedPlayers:
    print(x.name + (longestNameLength - len(x.name)) * ' ', x.memory)


def main():
  AddingPlayers()
  while (playercount > 4):
    Cycle()
  Finale()
  MemoryShit()


if __name__ == "__main__":
  main()
