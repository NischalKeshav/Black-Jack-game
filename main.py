import random, sys # modules
from art import logo #logo
print(logo)# create logo

 # deck of cards that is drawn from 
PlayerDeck= []
EnemyDeck = []
def card_give(deck,numOfcards=1):
  cards = [11,2,3,4,5,6,7,8,9,10,10,10]
  random.shuffle(cards)
  for i in range(numOfcards):  
    if cards[i]==11 and (sum(deck)+11)>=21:
      append = 1
    else:  
      append=(cards[i])
    deck.append(append)
  return append
def game():
  card_give(PlayerDeck,2)
  card_give(EnemyDeck,2)
print(EnemyDeck)
print(PlayerDeck)
EnemyScore = 0
PlayerScore = 0
cont = None
inputed = input ("Want to Play a game of BlackJack Y for yes, N for no")
if inputed.lower() == "n":
  sys.exit("Oh Well")
else:
  print("""  Lets Do THIS
  Best of Five! \n""")
  cont = True
while cont:
  game()
  sumOfenemy=sum(EnemyDeck)
  while sum(EnemyDeck) and sum(PlayerDeck) < 22:
    print(f"Enemy card: {EnemyDeck[0]}")
    if sumOfenemy <13:
      card_give(EnemyDeck,1)
    elif sumOfenemy<21 and (21-sumOfenemy) + random.randrange(0,7)>=6:
      card_give(EnemyDeck)
      if sum(EnemyDeck)>=22:
        break


    print(f"Your cards{PlayerDeck}")
    inputed = input("Draw a card? Y for yes, N for no:  ")
    if inputed.lower() == "y":
      print("You got a : "+str(card_give(PlayerDeck)))
    else:
      print ("You did not choose a card ")
  print(EnemyDeck)
  if sum(EnemyDeck)<22:#see who won
    print("You Lost!")
    EnemyScore += 1
  else:
    print("You won!")
    PlayerScore+=1
  print(f"You:{PlayerScore}  Opponent:{EnemyScore}")
  print("")
  if PlayerScore +EnemyScore==3:
    cont = False

  PlayerDeck=[]#reset
  EnemyDeck=[]#reset
if EnemyScore > PlayerScore:
  print("""Good job,
    But not good enough loser!!!!!""")
else:
  print("Good job You won!")









