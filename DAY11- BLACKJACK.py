#BLACKJACK CAPSTONE PROJECT
from replit import clear
logo_name = '''
██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

'''
print(logo_name)
import random
blackjack = True
while blackjack:
  j = q = k = 10 
  A = 0
  cards = [A,2,3,4,5,6,7,8,9,j,q,k] 

  player_card1 = random.choice(cards) 
  player_card2 = random.choice(cards) 
  player_set = [player_card1, player_card2]

  comp_card1 = random.choice(cards) 
  comp_card2 = random.choice(cards) 
  comp_set = [comp_card1, comp_card2]

  def value_of_ace():
    global A
    value = int(input("What value do you choose for ace...1 or 11?\n"))
    return value

  if "A" in player_set or "A" in comp_set:
    A = value_of_ace()

  player_score = sum(player_set)
  comp_score = sum(comp_set)

  game = True

  while player_score < 21 and comp_score < 21 and game:
    print(f"Your cards are {player_set}")
    print(f"Your current score is {player_score}")
    print(f"Computer's first card is {comp_card1}")

    player_decision = input("Enter 'y' to take another card. Enter 'n' to pass\n").lower()
    if player_decision == "y":
      player_cardn = random.choice(cards)
      player_set.append(player_cardn)
      if player_cardn == "A":
        A = value_of_ace()
      player_score = sum(player_set)
      print(f"Your cards are {player_set}")
      print(f"Your current score is {player_score}")
    elif player_decision == "n":
      comp_cardn = random.choice(cards)
      comp_set.append(comp_cardn)
      if comp_cardn == "A":
        A = value_of_ace()
      comp_score = sum(comp_set)
      print(f"The computer's cards are {comp_set}")
      print(f"The computer's current score is {comp_score}")

    if player_score <= 21 and comp_score <= 21:
      if player_score > comp_score:
        print("You are closer to 21, hence the winner!")
        game = False
      elif comp_score > player_score:
        print("The computer was closer to 21, hence you lose ")
        game = False


  if player_score > 21 and comp_score > 21:
    print("Both went over and lost...play again")
  elif player_score > 21:
    print("It's a bust for you...you lose")
  elif comp_score > 21:
    print("It's a bust for the computer...you win!")

  next_game = input("Do you want to play again?\ntype y or n").lower()
  if next_game == "y":
    clear()
  elif next_game == "n":
    clear()
    blackjack = False

print("Ok Goodbye!")

