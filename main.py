# Loop Assignment
from itertools import accumulate

print("Welcome to Taco Palace")
print("Please view the menu below and make a selection")
print("Taco Palace Menu:")
print("1.Taco")
print("2.Burrito")
print("3.Nachos")
print("4.Soft Drink")
print("5.Quit")


total = 0
list_of_inputs = []
choice = int(input("Pick a menu option: \n"))


while choice<5:
    print("1.Taco")
    print("2.Burrito")
    print("3.Nachos")
    print("4.Soft Drink")
    print("5.Quit")

    if choice == 1:
        list_of_inputs.append("Taco")
        total += 5.15
        print("You have selected: Taco")
    elif choice == 2:
        list_of_inputs.append("Burrito")
        total += 4.50
        print("You have selected: Burrito")
    elif choice == 3:
        list_of_inputs.append("Nachos")
        total += 3.65
        print("You have selected: Nachos")
    elif choice == 4:
        list_of_inputs.append("Soft Drink")
        total += 2.30
        print("You have selected: Soft Drink")
    elif choice == 5:
        print("Goodbye")

    choice = int(input("Pick a menu option: \n"))

ordered_items= ", ".join(list_of_inputs)
print("You ordered: " + ordered_items + ". Your total is ${}".format(total))





