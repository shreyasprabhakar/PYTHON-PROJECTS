#guess the number game
from replit import clear
import random

logo = '''
 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
'''
print(logo)
number_guessing = True
while number_guessing:
  print("welcome to the number guesing game")
  
  #choosing a random number to be guessed by the player
  numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
  random_number = random.choice(numbers)
  print("I am thinking of a number from 1 to 50")
  # print(random_number)
  
  #choosing difficulty level
  difficulty = input("choose a difficulty level ...'hard' or 'easy'.\n").lower()
  if difficulty == "hard":
    guesses = 5
    print("you have 5 chances to guess")
  elif difficulty == "easy":
    guesses = 10
    print("you have 10 chances to guess")
  else:
    print("invalid...run again")
    
  #main gameplay
  game = True
  for attempt in range(guesses + 1):
    if attempt in range(guesses) and game:
      player_guess = int(input("Guess my number"))
      if player_guess > random_number:
        print("too high!")
      elif player_guess < random_number:
        print("too low!")
      elif player_guess == random_number:
        game = False
        print("Correct guess!")
        
    elif attempt not in range(guesses) and game:
      game = False
      print("You are out of guesses :(")
          
  #asking whether player wants to play again
  play_again = input("do you want to play again...'y' or 'n'")
  if play_again == "y":
    clear()
  elif play_again == "n":
    clear() 
    number_guessing = False





