shoppingList = []

while True:
    print("Type any of the commands below")
    answer = input("print add remove stop\n")

    if answer == "stop":
        break
    if answer == "print":
        if len(shoppingList) != 0:
            for food in shoppingList:
                print(food)
        else:
            print("The shopping list does not have any food.")
    elif answer == "add":
        foodToAdd = input("Type what food you want to add\n")
        shoppingList.append(foodToAdd)
        print(foodToAdd, "was added to the shopping list")
    elif answer == "remove":
        for food in shoppingList:
            print(food, end=" ")
        removedFood = input("\nWhich food do you want to remove?\n")
        if removedFood in shoppingList:
            shoppingList.remove(removedFood)
            print(removedFood, "was removed from the list")
        else:
            print("That food cannot be found in the shopping list")

