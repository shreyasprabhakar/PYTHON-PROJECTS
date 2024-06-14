print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("You are at a crossroads. Do you want to go left or right? ")
dir = direction.lower()
if dir == "left":
          transport = input("you have reached the shore and need to get to the island...do you want to swim there or wait for a boat? ")
          tport = transport.lower()
          if tport == "wait":
                    door_color = input("You have reached the island and you see a house with three doors. Which door do you want to go into? Red, Blue or Yellow? ")
                    door = door_color.lower()
                    if door == "yellow":
                              print("You have found the treasure! You win!")
                    elif door == "red":
                              print("You have been burned by fire. boom roasted!.")     
                    elif door == "blue":
                              print("You have entered a lion cage. you dead bro.")
          elif tport == "swim":
                    print("And u jumped directly into Sharko's mouth. Aww he's relishing you. Anyway youse dead mate. Bye.")
elif dir == "right":
          print("you got carried away.......by a speeding truck. RIP:(. Game over.")
          

