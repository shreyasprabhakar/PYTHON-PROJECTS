rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
def rps_game():
  player_input =(input("You go first, type R for rock, P for paper, S for scissors "))
  lower_input = player_input.lower()

  if lower_input == "r":
      print("You have chosen ROCK")
      print (rock)
  elif lower_input == "p":
      print("You have chosen PAPER")
      print (paper)
  elif lower_input == "s":
      print("You have chosen SCISSORS")
      print (scissors)

  random_weapon = random.randint(0,2)

  if random_weapon == 0:
      print("The computer has chosen ROCK")
      print (rock)
  elif random_weapon == 1:
      print("The computer has chosen PAPER")
      print (paper)
  elif random_weapon == 2:
      print("The computer has chosen SCISSORS")
      print (scissors)

  final_pair = (str(lower_input) + str(random_weapon))
  if final_pair == "r2" or final_pair == "p0" or final_pair == "s1":
      last_line = ("You Won")
      print(last_line)
  elif final_pair == "r1" or final_pair == "p2" or final_pair == "s0":
      last_line = ("You Lost")
      print(last_line)
  elif final_pair == "r0" or final_pair == "p1" or final_pair == "s2":
      last_line = ("It's a TIE, Play Again")
      print(last_line)

while last_line == "You Won" or last_line == "You Lost" or last_line == "It's a TIE, Play Again":
  rps_game()

