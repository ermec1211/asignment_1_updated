def target_objectives():
    # Start with a predefined list of dishes. Each dish should be represented 
    # as a dictionary with the following keys:
    # name: A string representing the name of the dish.
    # calories: An integer representing the calorie count of the dish.
    # ingredients: A list of strings representing the ingredients. check

    # View All Dish Names:

    # Display a list of all the dish names in the inventory.
    # View Dish Details by Name:  check

    # Allow the user to input a dish name.
    # If the dish exists, display its details: name, calorie count, and ingredients.
    # If the dish does not exist, display an appropriate error message.
    # Filter Dishes by Calorie Count: check

    # Provide two separate options to:
    # View all dishes below a certain calorie threshold.
    # View all dishes above a certain calorie threshold.
    # Display the name, calorie count, and ingredients for all matching dishes. check
    # Add a New Dish:

    # Allow the user to input a new dish, including its name, calorie count, and ingredients (as a comma-separated list).
    # Add the new dish to the inventory.
    # Ensure that dish names are unique. If a dish with the same name already exists, prompt the user to enter a different name.
    # Remove a Dish by Name: check

    # Allow the user to specify the name of a dish to remove.
    # If the dish exists, remove it from the inventory.
    # If the dish does not exist, display an appropriate error message. check
    # Modify a Dish by Name:

    # Allow the user to specify a dish name to modify.
    # If the dish exists, present options to:
    # Change the dish’s name. check
    # Update its calorie count. check
    # Add new ingredients to the list. check
    # Remove specific ingredients from the list. check
    # If the dish does not exist, display an appropriate error message.
    # Search Dishes by Ingredient:

    # Allow the user to search for dishes containing a specific ingredient.
    # Display the names of all dishes that include the specified ingredient.
    # If no dishes match, display an appropriate message.
    # Exit the Program:

    # Provide an option to exit the loop and terminate the program

    #test
    pass


def updated_objectives():
    # updated program should use file io to store the dishes
    # store using a json file where the dishes are listed in the following way:
    # name: name of dish, calories: calorie count, ingredients: list of ingredients
    # open the file in read mode and loop through the file lines by putting the lines into varibles
    # once ou have a name var, calories var and ingrediants list
    # turn them into a dictionary and append them to a list
    pass


def file_exists(file_name):
    try:
        with open(file_name, "r") as file:
            return True
    except FileNotFoundError:
        return False
    

def put_dishes_into_dict(file_name):
    # this function is to take the file and go through each line so it can then put the correct things into a varible wich is then turned into a dictionary
    # when it reads "name:" in the file the next following is the name of the item.
    #the program will know when to stop with the name when it reads "." seperating the name from the next varible
    dishes = []
    dish_name = ""
    dish_calories = 0
    dish_ingredients = []
    i = 0
    with open(file_name, "r") as file:
        for line in file:
            if "name:" in line:
                dish_name = line.split(":").strip()
            elif "calories:" in line:
                dish_calories = int(line.split(":").strip())
            elif "ingredients:" in line:
                dish_ingredients = line.split(":").strip().split(",")
                dishes.append({
                    "name": dish_name,
                    "calories": dish_calories,
                    "ingredients": dish_ingredients
                })

def get_list_of_dishes(file_name):
    while True:
        print("what is the name of the file you would like to open?")
        file_name = input()
        if file_exists(file_name):
            dishes = put_dishes_into_dict(file_name)
            return dishes
        else:
            print("this file does not exist")
            print("please try again")
    


def is_digit(value):
    if value.isdigit():
        return True
    return False


def check_dish_exists(dishes, dish_name):
    for dish in dishes:
        if dish["name"] == dish_name:
            return True
    return False


def get_dish_index(dishes, dish_name):
    i = 0
    while i < len(dishes):
        if dishes[i]["name"] == dish_name:
            return i
        i += 1


def view_dish_details(dish):
    while True:
        print("what dish would you like to know more about?")
        dish_name = input().lower()
        if check_dish_exists(dish, dish_name):
            dish_index = get_dish_index(dish, dish_name)
            break
        print("this dish does not exist in the current menu")
        print("please try again")

    print("here is additional information about the dish")
    print(f"name: {dish[dish_index]['name']}")
    print(f"calories: {dish[dish_index]['calories']}")
    print(f"ingredients: {dish[dish_index]['ingredients']}")


def get_foods_below(dishes, max_calories):
    for dish in dishes:
        if dish["calories"] < max_calories:
            print(f"name: {dish['name']}")
            print(f"calories: {dish['calories']}")
            print(f"ingredients: {dish['ingredients']}")


def  get_foods_above(dishes, min_calories):
    for dish in dishes:
        if dish["calories"] > min_calories:
            print(f"name: {dish['name']}")
            print(f"calories: {dish['calories']}")
            print(f"ingredients: {dish['ingredients']}")


def choose_above_or_below(dishes):
    while True:
        print("would you like to see dishes above or below a certain calorie count?")
        print("1. below")
        print("2. above")
        choice = input()
        if choice == "1":
            print("what is the maximum calorie count?")
            max_calories = input()
            if is_digit(max_calories):
                max_calories = int(max_calories)
                get_foods_below(dishes, max_calories)
                break
            else:
                print("please enter a valid number")

        elif choice == "2":
            print("what is the minimum calorie count?")
            min_calories = input()
            if is_digit(min_calories):
                min_calories = int(min_calories)
                get_foods_above(dishes, min_calories)
                break  
            else:
                print("please enter a valid number")


def get_initial_dishes():
    """ returns the initial list of dishes""" 
    return [
        {
            "name": "rappie pie",
            "calories": 350,
            "ingredients": ["potato", "salt", "pepper", "cured pork", "chicken", "onion"]
        },
        {
            "name": "spaghetti carbonara",
            "calories": 560,
            "ingredients": ["spaghetti", "eggs", "pecorino cheese", "guanciale", "black pepper"]
        },
        {
            "name": "chicken caesar salad",
            "calories": 350,
            "ingredients": ["chicken breast", "romaine lettuce", "parmesan cheese", "croutons", "caesar dressing"]
        },
        {
            "name": "vegetable stir fry",
            "calories": 300,
            "ingredients": ["mixed vegetables", "tofu", "soy sauce", "garlic", "ginger", "vegetable oil"]
        }
]


def add_new_dish(dishes):
    print("what is the name of your dish?")
    
    while True:
        name = input().lower()
        if not check_dish_exists(dishes, name):
            break
        print("this dish already exists in the menu")
        print("please enter a new dish name")
    print("how many calories does the dish have?")
    while True:
        calories = input()
        if is_digit(calories):
            calories = int(calories)
            break
        else:
            print("please enter a valid number")
    print("please provide all of the ingrediants for your dish and when finished type 'done'")
    ingredients = []
    while True:
        print("enter an ingredient")
        ingredient = input().lower()
        if ingredient == "done":
            break
        ingredients.append(ingredient)
    
    new_dish = {
        "name": name,
        "calories": calories,
        "ingredients": ingredients 
    }

    dishes.append(new_dish)
        

def get_all_dish_names(dishes):
    for dish in dishes:
        print(dish["name"])


def remove_dish(dishes):
    while True:
        print("what dish would you like to remove?")
        dish_name = input().lower()
        if check_dish_exists(dishes, dish_name):
            dish_index = get_dish_index(dishes, dish_name)
            dishes.pop(dish_index)
            break
        else:
            print("this dish does not exist in the current menu")         


def change_dish_name(dishes, dish_index):
    print("what would you like to change the dish's name to?")
    new_name = input().lower()
    dishes[dish_index]["name"] = new_name


def change_calorie_count(dishes, dish_index):
    while True:
        print("what would you like to change the calorie count to?")
        new_calories = input()
        if is_digit(new_calories):
            new_calories = int(new_calories)
            dishes[dish_index]["calories"] = new_calories
            break
        else:
            print("please enter a valid number")


def add_new_ingredients(dishes, dish_index):
    while True:
        print("please provide all of the ingrediants for your dish and when finished type 'done'")
        input_ingrediants = input().lower()
        if input_ingrediants == "done":
            break
        dishes[dish_index]["ingredients"].append(input_ingrediants)


def remove_ingredients(dishes, dish_index):
    while True:
        print("what ingredient would you like to remove?")
        ingredient = input().lower()
        if ingredient in dishes[dish_index]["ingredients"]:
            dishes[dish_index]["ingredients"].remove(ingredient)
            break
        else:
            print("this ingredient is not in the list")
            print("please try again")


def modify_dish(dishes):
    while True:
        print("what dish would you like to modify?")
        dish_name = input().lower()
        if check_dish_exists(dishes, dish_name):
            dish_index = get_dish_index(dishes, dish_name)
            break
        else:
            print("this dish does not exist in the current menu")
            print("please try again")
    
    while True:
        print("what would you like to modify?")
        print("1. change the dish's name")
        print("2. update its calorie count")
        print("3. add new ingredients to the list")
        print("4. remove specific ingredients from the list")
        print("5. exit")
        
        choice = input()

        if choice == "1":
            change_dish_name(dishes, dish_index)
        elif choice == "2":
            change_calorie_count(dishes, dish_index)
        elif choice == "3":
            add_new_ingredients(dishes, dish_index)
        elif choice == "4":
            remove_ingredients(dishes, dish_index)
        elif choice == "5":
            break    
        else:
            print("invalid choice")
            print("please try again")


def search_dishes_by_ingredient(dishes):
    print("what ingredient would you like to search for?")
    ingredient = input().lower()
    for dish in dishes:
        if ingredient in dish["ingredients"]:
            print(dish["name"])
        print("there are no dishes that contain this ingredient")

       
def main():

    dishes = get_initial_dishes()

    print("welcome to the restaurant electronic menu")
    print("here are the current dishes that we are offering")
    get_all_dish_names(dishes)

    while True:
        print("what would you like to do?")
        print("1. view dish details")
        print("2. filter dishes by calorie count")
        print("3. add a new dish")
        print("4. remove a dish")
        print("5. modify a dish")
        print("6. search dishes by ingredient")
        print("7. get all dish names")
        print("8. exit the program")

        choice = input()
        if choice == "1":
            view_dish_details(dishes)
        elif choice == "2":
            choose_above_or_below(dishes)
        elif choice == "3":
            add_new_dish(dishes)
        elif choice == "4":
            remove_dish(dishes)
        elif choice == "5":
            modify_dish(dishes)
        elif choice == "6":
            search_dishes_by_ingredient(dishes)
        elif choice == "7":
            get_all_dish_names(dishes)
        elif choice == "8":
            print("exiting the program")
            break
        else:
            print("invalid choice")
        


if __name__ == "__main__":
    main()