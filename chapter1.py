import time
import random
import sys
import string
from colorama import Fore
from inputimeout import inputimeout, TimeoutOccurred
import datetime
from random import shuffle
import names
import webbrowser

def printdelay(predelay, text, delay):
  time.sleep(predelay)
  print(text)
  time.sleep(delay)

skip = input("enter E to skip, any other character to continue\n").lower()
if skip != "e":
  printdelay(1, 'Welcome to Rock Playing Game!', 2)
  printdelay(0, 'Version: 6.5.5', 2)
  printdelay(0, 'Chapter 1: The beginning of a new adventure', 2)
  printdelay(0, 'Made by Skeledan', 2)
  printdelay(
    0,
    'Everything is originally owned by Skeledan, and any other use of the content in this game is unauthorized without the consent of the owner, Skeledan.',
    2)
else:
  pass


def characterID(name, weapon, hp, itemsamount, dmg, comrades, amount):
  if Variables.amount_of_enemies == amount:
    Variables.amount_of_enemies -= 1
    Opponent.name = name
    Opponent.weapon = weapon
    Opponent.hp = hp
    Opponent.inithp = hp
    Opponent.itemsamount = itemsamount
    Opponent.dmg = dmg
    Opponent.comrade = comrades
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
      self.character_list = [
        'B-Hallpass', 'Paper Agent', 'The Flour God', 'Fat Cake', 'Paper Nuke',
        'Paper Queen', 'Scissor Emperor', 'Common Pasiaper', 'Rock Lord'
      ]

    def turn(self):
      self.stamina += 5
      if Opponent.dangermeterTrue == True:
        Opponent.dangermeteramount = Opponent.dangermeteramount - 1
        if Opponent.dangermeteramount == 1:
          print(Fore.RED + "One turn left to hide")
        else:
          print(Fore.WHITE + "Danger Meter: " +
                str(Opponent.dangermeteramount) + " turns left")
        if Opponent.dangermeteramount == 0:
          print(Opponent.comrade + " joined and killed you...")
          self.hp = self.hp - self.hp
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
      if Opponent.sans == True:
        Opponent.sansturns -= 1
        if Opponent.sansturns < 1:
          printdelay(0, self.truename + " did " + str(self.dmg) + " damage.",
                     3)
          Opponent.hp -= self.dmg
          printdelay(0, "Good job... Rock =)", 2)
          printdelay(0, "You earned 999999999999 gold and 9999999999999 EXP",
                     2)
          sansbattle = random.randint(100, 300)
          self.coins += sansbattle
          reset()
          mainselection()
        if Opponent.linger == True:
          self.hp -= Opponent.lingeringamount
          Opponent.lingerturns -= 1
      print(Fore.WHITE + Opponent.name + "'s Health: " + str(Opponent.hp))
      print("Your stats: Health: " + str(self.hp) + ' Damage: ' +
            str(self.dmg) + ' Stamina: ' + str(self.stamina) + ' Defense: ' +
            str(self.defense))
      time.sleep(2)
      if Opponent.dangermeterTrue == True and Opponent.dangermeteramount == 1 and Opponent.hp > 8:
        print("You feel like you need to sneak")
      if Opponent.dangermeterTrue == True and Opponent.dangermeteramount == 1 and Opponent.hp <= 8:
        print("You feel like you want to attack")
      if Opponent.finalboss == False:
        print('Choices are Attack, Item, Sneak, or Pass')
      self.choice = input('what will ' + self.truename + ' do? \n').lower()
      print(" ")
      if self.choice == 'attack':
        if Opponent.sans == True:
          print("You attacked with your knife")
          print("You missed!")
          Opponent.sansturns -= 1
        else:
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
      if self.choice == "sneak":
        if Opponent.dangermeterTrue == True:
          if Opponent.dangermeteramount == 1:
            chance = random.randint(1, 4)
            printdelay(0, Opponent.comrade + " came looking for you...", 4)
            if self.stamina < 10:
              print("You were too tired to sneak away")
              chance = 3
            if chance == 1 or 2:
              printdelay(0, Opponent.comrade + " couldn't find you!", 2)
              print(' ')
              Opponent.dangermeterTrue = False
              Opponent.dangermeteramount = random.randint(2, 9)
              battleLoop()
            if chance == 3 or 4:
              print("They found you!!")
              self.hp -= 60
              Player.turn()
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
      self.dangermeterTrue = False
      self.amountofitems = 12
      self.dangermeteramount = random.randint(4, 20)
      self.freeplay = False
      self.finalboss = False
      self.secretboss = False
      self.sans = False
      self.sansturns = random.randint(12, 25)
      self.lingeringamount = 9
      self.linger = False
      self.lingerturns = random.randint(1, 5)
      self.healthgain = 0

    def turn(self):
      if self.hp <= 0:
        print("You were victorious over " + Opponent.name + "!")
        if Opponent.finalboss == True:
          printdelay(0, "Gosh...", 2)
          printdelay(0, "Welp good game", 2)
          printdelay(
            0,
            "What you thought you defeated me? I'm literally the event itself",
            2)
          printdelay(0, "You have, thought, proven that you are a true rock!",
                     2)
          printdelay(0, "Or a really determined paper...", 2)
          restart = input("Do you want to start the next chapter\n? y/n/a")
          if restart == 'y' or restart == 'yes':
            exec(open('aftermain.py').read())
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
      if self.dangermeterTrue == True:
        opponentchoice = random.randint(1, 2)
        print(" ")
      if self.sans == True:
        opponentchoice = 1
      elif opponentchoice == 2:
        if self.amountofitems < 1:
          print(" ")
          opponentchoice = 1
      if self.hp < 60:
        opponentchoice = random.randint(1, 2)
      else:
        if Variables.amount_of_enemies <= 5:
          opponentchoice = random.randint(1, 4)
        if Variables.amount_of_enemies <= 3:
          opponentchoice = random.randint(1, 5)
        else:
          opponentchoice = random.randint(1, 3)
      if opponentchoice == 1:
        if self.sans == True:
          self.linger = True
          if Opponent.lingerturns > 1:
            Opponent.linger == False
            self.lingerturns = random.randint(1, 9)
          print(Opponent.name + " attacked " + "you with their " + self.weapon)
        if self.sans == False:
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
      if opponentchoice == 2:
        if self.name == "Fat Cake":
          if self.amountofitems == 0:
            print("Ate a lot of cupcakes")
            self.hp += 10
            Player.turn()

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
        print(self.name + " whistled for " + self.comrade + " to join!!")
        self.dangermeterTrue = True
        if self.finalboss == True:
          self.dangermeteramount += 10
        print("You have " + str(self.dangermeteramount) +
              " turns to kill or hide from the opponent!")
        self.dangermeteramount += 1
        print(" ")
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
  class modifiers:
    def __init__(self):
      print("In testing mode")
      
  Player = player()
  Opponent = opponent()
  Variables = variables()

  def reset():
    Opponent.name = "Opponent.name"
    Opponent.comrade = "Opponent.comrade"
    Opponent.hp = 100
    Opponent.dmg = 5
    Opponent.weapon = "Opponent.weapon"
    Opponent.dangermeterTrue = False
    Opponent.amountofitems = 12
    Opponent.dangermeteramount = random.randint(2, 9)
    Opponent.finalboss = False
    Opponent.secretboss = False
    Opponent.sans = False
    Opponent.sansturns = random.randint(12, 25)
    Opponent.lingeringamount = 5
    Opponent.linger = False
    Opponent.lingerturns = random.randint(1, 3)
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
    Opponent.dangermeteramount = random.randint(2, 9)
    Opponent.finalboss = False
    Opponent.secretboss = False
    Opponent.sans = False
    Opponent.sansturns = random.randint(12, 25)
    Opponent.lingeringamount = 5
    Opponent.linger = False
    Opponent.lingerturns = random.randint(1, 3)
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
      printdelay(predelay, Fore.RED + scrambled, postdelay)

    print(Fore.RED + "Error occured while loading 'menuselection()'")
    printdelay(0, "Attempeting to fix issue...", 5)
    printdelay(0, "Issue fixed, starting line 21", 4)
    skip = input(
      Fore.WHITE +
      "Type 'ɘ̷̧̢̗͚̭̎̏̍̓͘' to skip the introduction, type any other key to continue \n"
    )
    if skip.lower() == 'ɘ̷̧̢̗͚̭̎̏̍̓͘':
      print(Fore.RED + "...")
    shuffleletters(1, 'Welcome to Rock Playing Game!', 2)
    shuffleletters(0, 'Also known as RPG', 2)
    shuffleletters(0, 'version: ?', 2)
    shuffleletters(
      0,
      'Made by T̷̡̨͖̗̈̓͑̊̑ͅʜ̴͍͕̲̟̈́̓̈́̅̽͜ɘ̷̧̢̗͚̭̎̏̍̓͘T̴̯̻̥̤͆́̃͛̊͜ɿ̴̱̣̹̹͖̋͆̀̾́ὺ̵̧̜̯̹̞͐̈́̄̚ɘ̶̹͈͕̭́̓̉̿͠ͅƧ̵̢̢͕̖̤͊͒̇̿͝ʞ̸̨͈̣͕̲̆́̀̓̚ɘ̴̧̯̙̩͎̃̄̈̉̂l̵̡̧̡̻͂̐͒̀͘ͅɘ̵̜͕̣͇̺̓̈́͋̐͝b̶̢̻̙͍̼͒̈́̌̚ɒ̶̧͉̯͓͂̏̈́̀͂͜n̷͎͉͓͍̯̾̔͊͛̍',
      2)
    shuffleletters(
      0,
      'Everything is originally owned by T̷̡̨͖̗̈̓͑̊̑ͅʜ̴͍͕̲̟̈́̓̈́̅̽͜ɘ̷̧̢̗͚̭̎̏̍̓͘T̴̯̻̥̤͆́̃͛̊͜ɿ̴̱̣̹̹͖̋͆̀̾́ὺ̵̧̜̯̹̞͐̈́̄̚ɘ̶̹͈͕̭́̓̉̿͠ͅƧ̵̢̢͕̖̤͊͒̇̿͝ʞ̸̨͈̣͕̲̆́̀̓̚ɘ̴̧̯̙̩͎̃̄̈̉̂l̵̡̧̡̻͂̐͒̀͘ͅɘ̵̜͕̣͇̺̓̈́͋̐͝b̶̢̻̙͍̼͒̈́̌̚ɒ̶̧͉̯͓͂̏̈́̀͂͜n̷͎͉͓͍̯̾̔͊͛̍, and any other use of the content in this game is unauthorized without the consent of the owner, T̷̡̨͖̗̈̓͑̊̑ͅʜ̴͍͕̲̟̈́̓̈́̅̽͜ɘ̷̧̢̗͚̭̎̏̍̓͘T̴̯̻̥̤͆́̃͛̊͜ɿ̴̱̣̹̹͖̋͆̀̾́ὺ̵̧̜̯̹̞͐̈́̄̚ɘ̶̹͈͕̭́̓̉̿͠ͅƧ̵̢̢͕̖̤͊͒̇̿͝ʞ̸̨͈̣͕̲̆́̀̓̚ɘ̴̧̯̙̩͎̃̄̈̉̂l̵̡̧̡̻͂̐͒̀͘ͅɘ̵̜͕̣͇̺̓̈́͋̐͝b̶̢̻̙͍̼͒̈́̌̚ɒ̶̧͉̯͓͂̏̈́̀͂͜n̷͎͉͓͍̯̾̔͊͛̍.',
      2)
    shuffleletters(0, 'Choices are: ', 2)
    print('Finale')
    finalchoosing = input(Fore.RED + "Which one will you choose? \n").lower()
    printdelay(2, "...", 2)
    if finalchoosing == "finale":
      print(Fore.RED + "That's what I thought")
    else:
      print(Fore.RED + "Your choices don't matter anymore")
    print(" ")
    printdelay(
      0, Fore.RED + "Thank you for defeating EVERYONE that I wanted you to", 2)
    sys.stdout.write("\033[F")
    printdelay(
      0, Fore.RED + "Let's see if YOU can defeat me, shall we?            ", 2)
    sys.stdout.write("\033[F\033[K")
    printdelay(
      0, Fore.RED + "GOOD LUCK, YOU'LL NEED IT                            ", 1)
    sys.stdout.write("\033[F\033[K")
    time.sleep(2)
    printdelay(
      2, Fore.BLUE +
      "You didn't know if you were finally going to defeat this boss...", 0)
    sys.stdout.write("\033[F")
    printdelay(
      2, Fore.BLUE +
      "But you felt something glowing inside of you                        ",
      0)
    sys.stdout.write("\033[F\033[K")
    printdelay(
      2, Fore.BLUE +
      "You felt stronger, and more ready to finally end this game...   ", 2)
    Opponent.name = Fore.GREEN + 'T̷̡̨͖̗̈̓͑̊̑ͅʜ̴͍͕̲̟̈́̓̈́̅̽͜ɘ̷̧̢̗͚̭̎̏̍̓͘T̴̯̻̥̤͆́̃͛̊͜ɿ̴̱̣̹̹͖̋͆̀̾́ὺ̵̧̜̯̹̞͐̈́̄̚ɘ̶̹͈͕̭́̓̉̿͠ͅƧ̵̢̢͕̖̤͊͒̇̿͝ʞ̸̨͈̣͕̲̆́̀̓̚ɘ̴̧̯̙̩͎̃̄̈̉̂l̵̡̧̡̻͂̐͒̀͘ͅɘ̵̜͕̣͇̺̓̈́͋̐͝b̶̢̻̙͍̼͒̈́̌̚ɒ̶̧͉̯͓͂̏̈́̀͂͜n̷͎͉͓͍̯̾̔͊͛̍'
    Opponent.weapon = Fore.RED + 'ﻼ̶̪̥̟̗͓̍̏̂͋̆n̷̡̹̙̥͙͑̆͂͋̔ĭ̸̝̲͎͙̋͌̀̾ͅʇ̶͉͎͎̥̜͑̿͋̆͆ɘ̵̡̝͔͙̂͌̐͠͝ͅ'
    Opponent.hp = 99999
    Opponent.inithp = 99999
    Opponent.dmg = 50
    Opponent.initdmg = 50
    Opponent.comrade = Fore.BLUE + "⅃̷̻̥͍̦̱̉͒̿̾͘ȏ̵̹̤̣̰̣̃̏̎̑ƨ̴̡̳̺̘̒̅̾̾͝ͅɈ̸̧̘͕̹͕̿̑̔̇͝ ̵̢̳̞͎͈̽͊̎̉̊ƨ̷̛͖̟̺͖͙͋̑̇̀ô̸͎̫̩̺̾̀͑̐͜υ̵͓̞̘͔̙͊̂̉̔͝l̷͇̦̙̈́̏̈́̕̚ͅͅ"
    Player.dmg += Player.lvl * 6 - 3
    Player.dmg += Player.lvl * 6 - 3
    Player.hp += Player.lvl * 6 - 5
    Player.inithp += Player.lvl * 6 - 5
    Player.itemsamount = 20
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

  def tutorial():
    printdelay(0, "Hmm! Looks like you are a new rock", 2)
    printdelay(0, "Time to begin our training", 2)

    def keepTrue(attacktype, statement):
      while True:
        thingy = input("")
        lower = thingy.lower()
        if lower != attacktype:
          print(f"No, you need to type {attacktype}")
        if lower == 'stop' or lower == 'skip':
          printdelay(0, "Alright, if you think you're ready", 2)
          mainselection()
        else:
          printdelay(0, statement, 2)
          break

    printdelay(0, "First, we will begin with the opponent", 2)
    printdelay(2, "The opponent can fight, heal, or call for reinforcements",
               0)
    printdelay(0, "The player can attack, heal, sacrifice, and sneak", 2)
    print("First, attack the opponent, by typing 'Attack'")
    keepTrue("attack", f"{Player.truename} attacked the Test Dummy!")
    printdelay(0, "Next, type 'Item' to heal", 2)
    keepTrue("item", Player.truename + " ate a rock and healed 5 health!")
    printdelay(
      0,
      "Now 'sneak' is a way to skip your turn, have a chance to flee, and dodge the reinforcements when they come in",
      2)
    print("Now type 'Sneak'")
    keepTrue("sneak", Player.truename + " successfully snuck away!")
    printdelay(0, "Goodjob! Now you've escaped the opponent and won the game!",
               2)
    printdelay(
      0,
      "1 more thing to know: Use 'Upgrade' in the menu to upgrade your rock",
      2)
    printdelay(
      0, "Goodluck with this quest little rock, hope you defeat the papers!",
      2)
    mainselection()

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
    if Player.lorewrites == False:
      menuSelection = input(
        "Do you want to go to Tutorial, Prologue, Main Story, Grinder, Upgrader, or Skeledan? \n"
      ).lower()
    if Player.lorewrites == True:
      menuSelection = input(
        "Do you want to go to Main Story, Grinder, Upgrader, or Skeledan? \n"
      ).lower()
    if menuSelection == 'main story' and Player.freeplayunlock != True:
      print(
        "You have to defeat the Paper Soldier first! Go to Prologue and defeat them"
      )
      mainselection()
    if menuSelection == 'prologue' and Player.freeplayunlock == True:
      printdelay(0, "...", 1)
      print("You don't have a choice, you're going to main story")
      Player.lorewrites = True
      menuSelection = 'main story'
    if menuSelection == 'main story' and Player.freeplayunlock == True:
      menuSelection = "main story"
    if menuSelection == 'prologue':
      x = random.randint(2, 6)
      y = random.randint(3, 11)
      printdelay(0, "Locating the battle...", x)
      printdelay(0, "Located the battle! Travelling to the battle...", y)
      mainBattleStart()
    if menuSelection == 'tutorial':
      tutorial()
    if menuSelection == 'main story':
      if Variables.amount_of_enemies == 9:
        characterID('B-Hallpass', 'interdimensional nuke', 120, 11, 20,
                    "the paper watchers", 9)
        Variables.BHallPass = True
      if Variables.amount_of_enemies == 8:
        characterID("Paper Agent", "paper gun", 140, 12, 15, "Paper Soldiers",
                    8)
      if Variables.amount_of_enemies == 7:
        characterID('The Flour God', 'flour spray', 160, 13, 30,
                    "Bread and Cake", 7)
      if Variables.amount_of_enemies == 6:
        characterID('Paper chef', 'thick frosting', 180, 14, 35,
                    'chef minions', 6)
      if Variables.amount_of_enemies == 5:
        characterID('Paper Nuke', 'explosion', 10, 0, 9999, 'more nukes', 5)

      if Variables.amount_of_enemies == 4:
        characterID('Scissor Emperor', 'scissor snip', 1000, 16, 30,
                    'scissor knights', 3)
      if Variables.amount_of_enemies == 3:
        printdelay(2, 'YOU ARE A ROCK??', 2)
        characterID('Paper guard', 'paper spear', 1100, 17, 35, 'paper agents',
                    2)
      if Variables.amount_of_enemies == 2:
        characterID('Paper Queen', 'origami sword', 1200, 15, 25,
                    'paper soldiers', 4)
      if Variables.amount_of_enemies == 1:
        characterID('Rock Lord', 'rock staff', 260, 18, 60, 'rock guards', 1)

    if menuSelection == "secret":
      print(
        "It's an egregious night outside of the walls of this fine establishment known as the Hall Where Formal Judgement Occurs..."
      )
      sys.stdout.write("\033[F\033[K")
      time.sleep(2)
      print("The avian species are making chirpy noises           ")
      sys.stdout.write("\033[F\033[K")
      time.sleep(2)
      print("The angiosperms are blooming with their pods containing seeds")
      sys.stdout.write("\033[F\033[K")
      time.sleep(2)
      print(
        "On nights such as these, homosapiens sapiens under 18 such as you...")
      sys.stdout.write("\033[F\033[K")
      time.sleep(4)
      print(
        "SHOULD BE UNDERGOING A SEMIPLASMATIC CHEMICAL REACTION IN AN AREA BELEIVED TO BE WHERE EVIL GOES"
      )
      time.sleep(3)
      Opponent.name = 'Sir paper'
      Opponent.weapon = 'fancy cut'
      Opponent.hp = 1
      Opponent.inithp = 1
      Opponent.dmg = 1
      Opponent.comrade = "your death"
      Player.name = "Rock"
      Player.weapon = "not fake sharp object"
      Player.dmg = 9999999999999
      Player.hp = 92
      Opponent.sans = True
      battleLoop()
    if menuSelection == 'sus':
      print("YOU")
      sys.stdout.write("\033[F\033[K")
      time.sleep(2)
      print("ARE")
      sys.stdout.write("\033[F\033[K")
      time.sleep(2)
      print("SUS")
      sys.stdout.write("\033[F\033[K")
      time.sleep(2)
      characterID('Sus Rock', 'boom boom pow weapon', 200, 50, 'imposters')
      Opponent.name = 'Sus Rock'
      Opponent.weapon = 'boom boom pow weapon'
      Opponent.hp = 200
      Opponent.inithp = 200
      Opponent.dmg = 50
      Opponent.initdmg = 50
      Opponent.comrade = 'imposter'
      battleLoop()
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
    if menuSelection == 'grinder' and Player:
      confirmation = input("Are you ready to start the grind?\n")
      if confirmation == "y" or "yes":
        Opponent.hp = random.randint(50, 300)
        Opponent.inithp = Opponent.hp
        Opponent.dmg = random.randint(5, 20)
        Opponent.initdmg = Opponent.dmg
        Opponent.comrade = names.get_last_name()
        Opponent.weapon = "paper sword"
        Opponent.name = names.get_full_name()
        battleLoop()
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
    Player.truename = input("What is your name? \n")
    if Player.truename == "Skeledan":
      print("Hello Creator... Or Doppelganger")
    if Player.truename == "random":
      Player.truename = names.get_first_name()
    nameloop = True
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
  print(Fore.BLUE + "Hm?")
  printdelay(0, Fore.BLUE + "Oh hello there", 2)
  printdelay(0, Fore.BLUE + f"{Player.truename}, right?", 2)
  printdelay(0, Fore.BLUE + "...interesting", 2)
  buginput = input(Fore.BLUE + "You're here for a bug, correct? \n")
  printdelay(0, "Doesn't matter...", 2)
  printdelay(2, Fore.BLUE + "Try reporting this bug in the Discord server", 2)
  print(f"Here is the bug -> {e}")
  webbrowser.open('https://discord.gg/8DWB2Zzt3J')
  printdelay(2, Fore.BLUE + "I will now send you out of here", 2)
  printdelay(
    2, Fore.BLUE + "You have one more chance my fellow rock, make it count", 2)
  mainselection()