import Sprite
import GameRule
import os

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
spacer = ' ' *  5
damage = 50
game = True 

def printElement():
  for pieces in zip(*(AllSprite.splitlines() for AllSprite in AllSprite)):
    print(spacer.join(pieces))


# Player select their pokemon
P1_selection = input("P1 choose your pokemon ! ").lower()
if P1_selection == "shinx":
   PokemonClassP1 = Sprite.Shinx
elif P1_selection == "charmender":
   PokemonClassP1 = Sprite.Charmender

P2_selection = input("P2 choose your pokemon ! ").lower()
if P2_selection == "shinx":
   PokemonClassP2 = Sprite.Shinx
elif P2_selection == "charmender":
   PokemonClassP2 = Sprite.Charmender

AllSprite = PokemonClassP1.spriteBack, PokemonClassP2.spriteFront

printElement()

while game == True:
  print('\r' + PokemonClassP1.name, ":", PokemonClassP1.actualpv, "/", PokemonClassP1.maxpv)
  print('\r' + "Choose your move ! : " ,"Volt switch", "|", "Wild Charge","|", "Thief","|", "Fire Fang")
  print('\r' + PokemonClassP2.name, ":", PokemonClassP2.actualpv, "/", PokemonClassP2.maxpv)
  P1Action = input("What will " + PokemonClassP1.name + " do ? :").lower()
  if P1Action == "volt switch":
     PokemonClassP2.actualpv = PokemonClassP2.actualpv - GameRule.damageCalculation(PokemonClassP1.level, PokemonClassP1.voltswitch[1], PokemonClassP1.spAttack, PokemonClassP2.spDefense, 1.5, 1, 1)
  P2Action = input("What will " + PokemonClassP2.name + " do ? :").lower()
  
  os.system('cls')
  printElement()
  if PokemonClassP1.actualpv <= 0:
    game = False
    print(PokemonClassP1.name + " a perdu ! ")
  elif PokemonClassP2.actualpv <= 0:
     game = False
     print(PokemonClassP2.name + " a perdu ! ")

  
  


