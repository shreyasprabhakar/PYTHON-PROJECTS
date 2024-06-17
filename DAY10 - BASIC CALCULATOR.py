logo_name = '''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
'''
logo = '''
 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
next_step = ""
output = ""
calc = True
print(logo)
print(logo_name)
while calc:
  num1 = float(input("Enter your first number "))
  num2 = float(input("Enter your second number "))

  #the loop function for continuing operating on the previous output
  def continue_loop():
    global next_step
    global output
    for operator in operations:
      print(operator)

    req_op = input("Select an operation(Strictly do not input anything other than the above 4 options) ")

    if req_op in operations:
      output = int(operations[req_op](num1, num2))
      print(output)

    next_step = input("Enter 'continue' to operate further on this output. Enter 'new' to clear and start new calculation page.\nStrictly do not type anything but one of the two options given above.\n").lower()

  #initially calling the loop for the first calculation
  continue_loop()

  while next_step == "continue":
    num1 = float(output)
    num2 = float(input("Enter the other number "))
    #calling the loop for continuing the operation with the previous output
    continue_loop()

  if next_step == "new":
    clear()



  
  
  
  


           
