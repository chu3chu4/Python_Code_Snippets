"""
direction = input("which direction do you want to go: ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "west":
        print ("left")
    case "east":
        print ("right")
    case _:
        print ("that's not a valid direction")
"""

user_choise = int(input("provide a number between 1 and 3: "))

match user_choise:
    case 1:
        print("One")
    case 2:
        print ("Two")
    case 3:
        print("Three")
    case _:
        print("that's a wrong number")