#WORK IN PROGRESS

import time
import random
import sys
import string
from colorama import Fore
from inputimeout import inputimeout, TimeoutOccurred
import datetime
from random import shuffle
import webbrowser
import chapter1

def printdelay(predelay, text, delay):
  time.sleep(predelay)
  print(text)
  time.sleep(delay)

print("Welcome to Chapter 2: The rise of the Oragami")

def characterID(name, weapon, hp, itemsamount, dmg, amount):
  if Variables.amount_of_enemies == amount:
    Variables.amount_of_enemies -= 1
    Opponent.name = name
    Opponent.weapon = weapon
    Opponent.hp = hp
    Opponent.inithp = hp
    Opponent.itemsamount = itemsamount
    Opponent.dmg = dmg
    Opponent.potiondmg = amount
    x = random.randint(2, 6)
    y = random.randint(3, 11)
    printdelay(0, "Locating the battle...", x)
    printdelay(0, "Located the battle! Travelling to the battle...", y)
    mainBattleStart()


try:
  time.sleep(2)
  t0 = time.time()

  seconds = time.time()

  class player:

    def __init__(self):
      self.truename = " "
      self.hp = int(100)
      self.inithp = 100
      self.deaths = 0
      self.stamina = 95
      self.lvl = 0
      self.dmg = 5
      self.initdmg = 5
      self.defense = 10
      self.initdefense = 10
      self.eventamount = 3
      self.lorewrites = False
      self.weapon = 'fist'
      self.name = ' '
      self.coins = int(40)
      self.sneaksuccess = False
      self.skipturns = 0
      self.itemsamount = 10
      self.freeplayunlock = False
      self.cheatpoints = 0
      self.loop = True
      self.coinsbonus = False

    def turn(self):
      self.stamina += 5
      if self.hp > self.inithp:
        self.hp = self.inithp
      if self.stamina >= 100:
        self.stamina = 100
      if self.stamina <= 0:
        self.stamina = 0
      if Opponent.hp > Opponent.inithp:
        Opponent.hp = Opponent.inithp
      if self.hp <= 0:
        printdelay(0, Opponent.name + " defeated " + Player.truename, 6)
        if Opponent.finalboss == True:
          print("You loser...")
          printdelay(2, "Don't you dare escape", 2)
          printdelay(0, "TIME TO USE finale()", 2)
          finale()
          printdelay(2, "INIATE battleLoop()", 2)
          battleLoop()
          printdelay(0, "battle has been rewritten again...", 5)
        deathscreen()
        self.deaths += 1
        mainselection()
      print(Fore.WHITE + Opponent.name + "'s Health: " + str(Opponent.hp))
      print("Your stats: Health: " + str(self.hp) + ' Damage: ' +
            str(self.dmg) + ' Stamina: ' + str(self.stamina) + ' Defense: ' +
            str(self.defense))
      time.sleep(2)
      if Opponent.finalboss == False:
        print('Choices are Attack, Item, Sneak, or Pass')
      self.choice = input('what will ' + self.truename + ' do? \n').lower()
      print(" ")
      if self.choice == 'attack':
        chancehit = random.randint(0, 30)
        staminaloss = random.randint(10, 20)
        if Variables.amount_of_enemies <= 8:
          staminaloss = random.randint(20, 30)
        if Variables.amount_of_enemies <= 5:
          staminaloss = random.randint(20, 40)
        attackvariation = random.randint(0, 7)
        if Opponent.finalboss == True:
          attackvariation = random.randint(50, 100)
        totalAttack = self.dmg
        totalAttack += attackvariation
        if self.stamina < 10:
          print("You were too tired to attack!")
          totalAttack = 0
        if chancehit >= 25:
          totalAttack = totalAttack + 10
          print("You did a critical hit!!")
        if chancehit <= 5:
          totalAttack = 0
          print("The attack was too slow!")
        print("You attacked " + Opponent.name + " with your " + self.weapon)
        print("You did " + str(totalAttack) + " damage!")
        Opponent.hp = Opponent.hp - totalAttack
        self.stamina = self.stamina - staminaloss
        print(' ')
        Opponent.turn
      if self.choice == 'pass':
        staminaAddition = random.randint(20, 50)
        print("You stood and rested")
        print("You gained back ", staminaAddition, " stamina")
        print(" ")
      if self.choice == 'item':
        totalitems = self.itemsamount
        healamount = random.randint(20, 30)
        item = " "
        healitem = random.randint(1, 3)
        if healitem == 1:
          item = "banana"
          healamount = healamount + 10
          self.stamina = self.stamina + 20
        if healitem == 2:
          item = "chocolate bar"
          healamount = healamount + 14
          self.stamina = self.stamina + 40
        if healitem == 3:
          item = "human limb"
          healamount = healamount + 18
          self.stamina = self.stamina + 60

        print("You have " + str(totalitems) + " items")
        if totalitems < 1:
          healamount = 5
          printdelay(
            0,
            "You rummaged through your sack, but found no items left to consume",
            2)
          printdelay(1, "You decided to pick a rock from the ground", 0)
          print("It was edible? Healed ", str(healamount))
          self.hp = self.hp + healamount
          if self.hp > self.inithp:
            print("Your health maxed out!")
          self.stamina += 10
        if totalitems > 1:
          healconfirm = input("Do you want to heal?\n")
          if healconfirm == 'y' or 'yes':
            print("You rummaged through your sack and found a " + item + "!")
            print("You ate it and healed " + str(healamount) + " health!")
            Player.hp += healamount
            self.itemsamount -= 1

          else:
            pass
          print(' ')
        chance = random.randint(1, 20)
        if self.stamina < 10:
          chance = 10
        if Opponent.finalboss == True:
          chance = 20
        if Opponent.finalboss == False:
          if chance >= 5:
            print("You couldn't hide and the opponent found them")
            Opponent.turn()
          else:
            print("You hid successfully!")
            self.sneaksuccess = True
        print(" ")

  class opponent:

    def __init__(self):
      self.name = " "
      self.freeplayname = False
      self.comrade = " "
      self.hp = 100
      self.inithp = 100
      self.dmg = 5
      self.weapon = " "
      self.amountofitems = 12
      self.potiondmg = 5
      self.freeplay = False
      self.finalboss = False
      self.secretboss = False
      self.healthgain = 0

    def turn(self):
      if self.hp <= 0:
        print("You were victorious over " + Opponent.name + "!")
        if Opponent.finalboss == True:
          printdelay(0, "NOOOOOOOOOOOO", 2)
          printdelay(0, "Watch, you'll see!!", 2)
          printdelay(0, "I'll be back soon...", 2)
          restart = input("Do you want to restart the game\n? y/n/a")
          if restart == 'y' or restart == 'yes':
            Player.freeplayunlock = False
            Variables.amount_of_enemies = 10
            printdelay(0, "Restarting...", 2)
          if restart == 'n' or restart == 'no':
            t1 = time.time()
            print("Your speedrun time was: " + str(round((t1 - t0) * 2)) +
                  " seconds")
            print("Have a good one, alright?")
            time.sleep(2)
            quit("Rock.webp")
        Player.coins = Player.coins + ((Player.dmg - 2) + Player.hp +
                                       Opponent.dmg + 20) + Player.itemsamount
        print("You now have " + str(Player.coins) + " quartz")
        if self.name == "Paper Soldier" and Variables.amount_of_enemies == 10:
          Variables.amount_of_enemies -= 1
          Player.freeplayunlock = True
          printdelay(0, "Main story unlocked!", 1)
        printdelay(0, "Returning to main menu...", 3)
        self.hp = 100
        reset()
        mainselection()
      if Variables.amount_of_enemies <= 5:
        opponentchoice = random.randint(1, 4)
      if Variables.amount_of_enemies <= 3:
        opponentchoice = random.randint(1, 5)
      else:
        opponentchoice = random.randint(1, 3)
      if opponentchoice == 2:
        if self.amountofitems < 1:
          print(" ")
          opponentchoice = 1
      if opponentchoice == 2 and self.hp >= (self.inithp / 2):
        opponentchoice = 1
      else:
        if Variables.amount_of_enemies <= 5:
          opponentchoice = random.randint(1, 4)
        if Variables.amount_of_enemies <= 3:
          opponentchoice = random.randint(1, 5)
        else:
          opponentchoice = random.randint(1, 3)
      if opponentchoice == 1:
        chancehit = random.randint(0, 30)
        attackvariation = random.randint(5, 25)
        totalAttack = self.dmg
        totalAttack += attackvariation - (Player.defense / 2)
        if chancehit >= 25:
          totalAttack = totalAttack + 10
          print(self.name + " did a critical hit!!")
        if chancehit <= 5:
          totalAttack = 0
          if totalAttack <= 0:
            print("You dodged " + self.name + "'s attack!")
        print(Opponent.name + " attacked " + "you with their " + self.weapon)
        print(self.name + " did " + str(totalAttack) + " damage!")
        Player.hp = Player.hp - totalAttack
        print(' ')

        item = "power bar"
        itemgain = random.randint(1, 20)
        itemname = random.randint(1, 3)
        if itemname == 1:
          item = "chocolate bar"
          self.healthgain = 10
        if itemname == 2:
          item = "banana"
          self.healthgain = 5
        if itemname == 3:
          item = "power core"
          self.healthgain = 15
        self.healthgain = self.healthgain + itemgain
        print(self.name + " used " + item + "!")
        print(Opponent.name + " healed " + str(self.healthgain) + " health!")
        self.hp = self.hp + self.healthgain
        self.amountofitems = self.amountofitems - 1
        print(" ")
      if opponentchoice == 3:
        print(" ")
        attackvariation = random.randint(-5, 20)
        totaldmg = self.potiondmg + attackvariation
        print(f"{self.name} threw a potion at you")
        if totaldmg == 0:
          print("You felt no pain!")
        if totaldmg < 0:
          print("The potion regained your health!")
          Player.hp += totaldmg
        else:
          print(f"You took {totaldmg} damage!")
        print()
      if opponentchoice == 4:
        try:
          a = random.randint(1, 15)
          b = random.randint(1, 15)
          answer = inputimeout(prompt=f'What is {str(a)} * {str(b)}\n',
                               timeout=10)
        except TimeoutOccurred:
          Player.hp -= round(a * 1.5)
        if int(answer) == int(a * b):
          print("Correct!")
          Player.stamina += 20
      if opponentchoice == 5:
        print(Opponent.name +
              " initiated a engine crisis! You have 5 seconds to fix it!")
        letters = string.digits
        length = 5
        theresult = ''.join(random.choice(letters) for i in range(length))
        print("The password is: " + str(theresult))
        try:
          playerpassword = inputimeout(
            prompt="Type the password to fix it! \n", timeout=5)
          if str(playerpassword) == int(theresult):
            print("Correct password!")
            Player.turn
          if str(playerpassword) != str(theresult):
            print("Incorrect password!")
            print("Health is divided by half")
            Player.hp /= 2
            Player.turn
        except Exception:
          playerpassword = "It's too late!"
          print(playerpassword)
          Player.hp /= 2

        print(" ")

      Player.turn

  class variables:

    def __init__(self):
      self.amount_of_enemies = 10
      self.randomname = False

  Player = player()
  Opponent = opponent()
  Variables = variables()

  def reset():
    Opponent.name = "Opponent.name"
    Opponent.comrade = "Opponent.comrade"
    Opponent.hp = 100
    Opponent.dmg = 5
    Opponent.weapon = "Opponent.weapon"
    Opponent.amountofitems = 12
    Opponent.finalboss = False
    Opponent.secretboss = False
    Player.hp = Player.inithp
    Player.stamina = 95
    Player.dmg = Player.initdmg
    Player.defense = Player.defense
    Player.sneaksuccess = False
    Player.skipturns = 0
    Player.itemsamount = 10

  def deadreset():
    Opponent.hp = Opponent.inithp
    Opponent.dangermeterTrue = False
    Opponent.amountofitems = 12
    Opponent.finalboss = False
    Opponent.secretboss = False
    Player.hp = Player.inithp + 2
    Player.defense = Player.initdefense
    Player.dmg = Player.initdmg + 2
    Player.stamina = 95
    Player.sneaksuccess = False
    Player.skipturns = 0
    if Player.itemsamount < 10:
      Player.itemsamount = 10
    Player.dmg += 2

  def battleLoop():
    battleLoop = True
    while battleLoop == True:
      Player.turn()
      Opponent.turn()

  def mainBattleStart():
    if Variables.amount_of_enemies == 10:
      Opponent.name = "Paper Soldier"
      Opponent.comrade = "Paper Agent"
      Opponent.weapon = "a paper cut"
    if Opponent.finalboss == True:
      pass
    print("Rockiness level is " + str(Player.lvl))
    Player.dmg += Player.lvl * 4 - 3
    Player.dmg += Player.lvl * 4 - 3
    Player.hp += Player.lvl * 4 - 5
    Player.inithp += Player.lvl * 4 - 5
    printdelay(
      0, "You were walking through the paper kingdom, when " + Opponent.name +
      " stopped you", 2)
    print("Battle started!")

    battleLoop()

  def finale():

    def shuffleletters(predelay, string, postdelay):
      thestring = list(string)
      shuffle(thestring)
      scrambled = ''.join(thestring)

    print(Fore.RED + "...")
    shuffleletters(1, 'Rock Playing Game Chapter 2', 2)
    shuffleletters(0, '....', 2)
    shuffleletters(0, 'Bugged', 2)
    shuffleletters(0, '', 2)
    shuffleletters(0, 'Choices are: ', 2)
    print('bug')
    print(" ")
    printdelay(0, Fore.RED + "I had ENOUGH with your shenaniganse", 2)
    sys.stdout.write("\033[F")
    printdelay(0, Fore.RED + "Bugs over and OVER again that I HAVE to fix", 2)
    sys.stdout.write("\033[F\033[K")
    printdelay(0, Fore.RED + "TIME TO END THIS                            ", 1)
    sys.stdout.write("\033[F\033[K")
    time.sleep(2)
    printdelay(
      2, Fore.BLUE + "Another chapter... were you going to win this again?", 0)
    sys.stdout.write("\033[F")
    printdelay(
      2, Fore.BLUE +
      "But you felt something glowing inside of you                        ",
      0)
    sys.stdout.write("\033[F\033[K")
    printdelay(
      2, Fore.BLUE +
      "You felt stronger, and more ready to finally end this game...   ", 2)
    Opponent.name = Fore.GREEN + 'Glitched'
    Opponent.weapon = Fore.RED + 'bugs'
    Opponent.hp = 100000
    Opponent.inithp = 100000
    Opponent.dmg = 55
    Opponent.initdmg = 55
    Opponent.potiondmg = 20
    Player.dmg += Player.lvl * 8 - 3
    Player.dmg += Player.lvl * 8 - 3
    Player.hp += Player.lvl * 8 - 5
    Player.inithp += Player.lvl * 8 - 5
    Player.itemsamount = 30
    Opponent.finalboss = True
    battleLoop()

  def deathscreen():
    printdelay(0, Fore.GREEN + "Well... hello", 2)
    printdelay(0, "Welcome to function deathscreen()", 2)
    printdelay(2, "...", 2)
    printdelay(0, "You are a rock, not a paper", 2)
    printdelay(0, Fore.RED + "I'll revive you, don't you dare die again", 1)
    deadreset()
    battleLoop()
    time.sleep(2)
    Player.deaths += 1

  def mainselection():
    reset()
    time.sleep(2)
    if Variables.amount_of_enemies != 0:
      if Variables.amount_of_enemies <= 3:
        print(Fore.RED, f"{Variables.amount_of_enemies}, left...")
      else:
        print(Fore.WHITE, Variables.amount_of_enemies, "left...")
    if Variables.amount_of_enemies == 0:
      finale()
    print(Fore.WHITE + "You have " + str(Player.coins) + " quartz")
    print("You died " + str(Player.deaths) + " times.")
    print("Your level is " + str(Player.lvl))
    menuSelection = input(
      "Do you want to go to Main Story, Upgrader, or Skeledan? \n").lower()
    if menuSelection == 'main story':
      if Variables.amount_of_enemies == 10:
        characterID('the paper guard', 'paper knife', 120, 10, 20, 2)
      if Variables.amount_of_enemies == 9:
        characterID('A-Hallpass', 'finale nuke', 150, 14, 22, 9)
        Variables.BHallPass = True
      if Variables.amount_of_enemies == 8:
        characterID("Corrupted Paper", "paper gun", 160, 12, 20, 8)
      if Variables.amount_of_enemies == 7:
        characterID('Origami construction', 'flour spray', 170, 24, 30, 7)
      if Variables.amount_of_enemies == 6:
        characterID(
          'The doorkeeper',
          'thick frosting',
          190,
          13,
          35,
          6,
        )
      if Variables.amount_of_enemies == 5:
        characterID('Interdimensional Nuke', 'explosion', 10, 0, 9999, 0, 5)
      if Variables.amount_of_enemies == 4:
        characterID('Origami soldiers', 'nives', 500, 15, 40, 8)
      if Variables.amount_of_enemies == 3:
        characterID('Origami Prince', 'paper ray', 700, 16, 45, 9)
      if Variables.amount_of_enemies == 2:
        characterID('Corrupted Rock', 'rock', 1000, 17, 50, 10)
      if Variables.amount_of_enemies == 1:
        characterID('Paper overlord', 'death ray', 1200, 18, 60, 14)
    if menuSelection == "firstrock":
      currentDate = datetime.date.today()
      trueDate = datetime.date(2024, 7, 13)
      if currentDate == trueDate:
        characterID("First Rock", "Rock", 10000, 20, 30, "Second rocks", 3)
      else:
        print('It is not time yet')
    if menuSelection == "upgrader":
      print("Upgrade your rockiness")
      time.sleep(1)
      if Player.lvl == 0:
        amountofcoins = 100 + (5 * Player.lvl + 10)
      if Player.lvl > 0:
        amountofcoins = 100 + (2 * (Player.lvl + 15))
      print("To upgrade, it costs " + str(amountofcoins) + " quartz.")
      time.sleep(2)
      purchase = input("Do you want to buy it? y/n \n")
      if purchase == "y" or "yes":
        if Player.coins < amountofcoins:
          printdelay(1, "Sorry, you need more quartz.", 2)
          printdelay(0, "How can a rock be so poor...", 1)
          mainselection()
        else:
          Player.lvl += 1
          print("You have now reached level " + str(Player.lvl) + "!")
          Player.coins -= amountofcoins
          mainselection()
      else:
        print("Exited...")
    if menuSelection == 'skeledan':
      linkSelection = input('Youtube, Discord, Twitter, or Soundcloud').lower()
      if linkSelection == 'youtube':
        webbrowser.open('https://www.youtube.com/@therealskeledan')
      if linkSelection == 'discord':
        webbrowser.open('https://discord.gg/8DWB2Zzt3J')
      if linkSelection == 'soundcloud':
        webbrowser.open('https://soundcloud.com/rishi-aluru')
      if linkSelection == 'twitter':
        webbrowser.open('https://twitter.com/TheRealSkeledan')
    else:
      printdelay(0, "That isn't available! Please check your spelling!", 2)
      mainselection()

  nameloop = False
  while nameloop == False:
    name = input("What is your name? \n")
    Player.truename = name
    print("Welcome fellow Rock Apprentice, " + Player.truename)
    while True:
      classarray = [
        'Igneous', 'Sedimentary', 'Metamorphic', 'Normal', 'Rock hard', 'Paper'
      ]
      printdelay(2, "You need to choose your class! Here are the options:", 2)

      def classID(hp, dmg, weapon, defense):
        Player.hp = hp
        Player.inithp = hp
        Player.dmg = dmg
        Player.initdmg = dmg
        Player.defense = defense
        Player.initdefense = defense
        Player.weapon = weapon
        if Opponent.finalboss == True:
          Player.dmg *= 2
          Player.initdmg = Player.dmg
          Player.hp *= 2
          Player.inithp = Player.hp
          Player.defense *= 1.5
          Player.initdefense = Player.defense

      for classes in classarray:
        print(classes)
      print(' ')
      while True:
        player_class = input("What class are you? \n").lower()
        if player_class == "igneous" or player_class == 'i':
          classID(110, 25, 'firey explosion', 5)
          print("Selected Igneous")
          break
        if player_class == "sedimentary" or player_class == 's':
          classID(130, 20, 'rock wash', 10)
          print("Selected Sedimentary")
          break
        if player_class == "metamorphic" or player_class == 'm':
          classID(90, 23, 'pressured attack', 15)
          print("Selected Metamorphic")
          break
        if player_class == "rock hard" or player_class == 'r':
          classID(50, 6, 'air', 0)
          print("Selected Rock Hard")
          break
        if player_class == "normal" or player_class == 'n':
          classID(100, 15, 'fist', 10)
          print("Selected Normal")
          break
        elif player_class == "paper" or player_class == 'failure' or player_class == 'p':
          print("Selected Paper")
          classID(25, 0.5, 'failure', 0)
          break
        else:
          printdelay(2, "That isn't an available class!", 2)
          printdelay(0, "Please try one of the ones listed", 2)
      mainselection()
  time.sleep(2)

except Exception as e:
  printdelay(0, Fore.GREEN + "You again?", 2)
  printdelay(0, f"I'm not sure what is happening...", 2)
  printdelay(0, "Doesn't matter...", 2)
  printdelay(2, "Please report this bug in the Discord server", 2)
  print(f"Here is the bug -> {e}")
  webbrowser.open('https://discord.gg/8DWB2Zzt3J')
  printdelay(2, "Be careful, the plates are shifting", 2)
  printdelay(2, "One more chance, please fight my rock apprentice", 2)
  mainselection()