from clear import clear
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

logo = '''
 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗  
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝
                                                 
'''

# initial resources
water = 300
milk = 200
coffee = 100
money = 0


# function for checking for resources, modifying resources based on coffee flavour and printing the cost
def type_of_coffee(flavour):
    global water
    global milk
    global coffee
    global money
    if water >= int(menu[flavour]["ingredients"]["water"]):
        if milk >= int(menu[flavour]["ingredients"]["milk"]):
            if coffee >= coffee - int(menu[flavour]["ingredients"]["coffee"]):
                water = water - int(menu[flavour]["ingredients"]["water"])
                milk = milk - int(menu[flavour]["ingredients"]["milk"])
                coffee = coffee - int(menu[flavour]["ingredients"]["coffee"])
                money = money + round((menu[flavour]["cost"]), 2)
                print(f"That'll be ${round((menu[flavour]["cost"]), 2)}")

                # taking payment
                print("Enter the count of the following denominations you would like to pay")
                dollars = float(input("How many dollars? "))
                quarters = float(input("How many quarters?")) * 0.25
                dimes = float(input("How many dimes?")) * 0.10
                nickels = float(input("How many nickels?")) * 0.05
                money_recd = round((dollars + quarters + dimes + nickels), 2)
                if money_recd > round((menu[flavour]["cost"]), 2):
                    change = money_recd - round((menu[flavour]["cost"]), 2)
                    print(f"Here's your change ${change}")
                elif money_recd < round((menu[flavour]["cost"]), 2):
                    print("Amount not enough, money refunded")
                else:
                    print(f"Thank you, enjoy your {flavour}")

            else:
                print("Insufficient Ingredients")
        else:
            print("Insufficient Ingredients")
    else:
        print("Insufficient Ingredients")



print(logo)
machine = True
while machine:
    choice = input("Hey, what would you like to order...Espresso/Latte/Cappuccino?\n").lower()
    if choice == "report":
        print(f"water = {water}\n"
              f"milk = {milk}\n"
              f"coffee = {coffee}\n"
              f"money = {money}\n")
    elif choice == "espresso":
        type_of_coffee("espresso")
    elif choice == "latte":
        type_of_coffee("latte")
    elif choice == "cappuccino":
        type_of_coffee("cappuccino")
    elif choice == "turn off":
        clear()
        machine = False

    again = input("would you like to order again...y or n\n").lower()
    if again == "y":
        clear()
    elif again == "n":
        clear()
        machine = False

