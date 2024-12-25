favourite_food = []  # an empty list for adding favourite foods

while True:
    print("\nFavourite Food Manager")
    print("0. Exit")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View all favourite foods")
    
    choice = input('Choose an option: ')  # for taking user input
    
    if choice == "0":
        print("Thanks for using Favourite Food Manager")
        break
    
    elif choice == "1":
        food_input = input("Enter your favourite food names (separate by commas): ")
        foods = food_input.split(",")  # Split input by commas
        for food in foods:
            food = food.strip()  # Remove any leading/trailing whitespace
            favourite_food.append(food)
        print(f"{', '.join(foods)} added successfully")
    
    elif choice == "2":
        food_input = input("Enter the food names you want to remove (separate by commas): ")
        foods = food_input.split(",")
        for food in foods:
            food = food.strip()  # Remove any leading/trailing whitespace
            if food in favourite_food:
                favourite_food.remove(food)
                print(f"{food} removed successfully")
            else:
                print(f"{food} not found in the list")
    
    elif choice == "3":
        if favourite_food:
            print("Your favourite foods:")
            for index, food in enumerate(favourite_food, start=1):
                print(f'{index}. {food}')
        else:
            print("Food list is empty or no foods have been added yet")
    
    else:
        print("Invalid choice. Please select a valid option.")
