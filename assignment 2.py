def target_objectives():
    # Start with a predefined list of dishes. Each dish should be represented 
    # as a dictionary with the following keys:
    # name: A string representing the name of the dish.
    # calories: An integer representing the calorie count of the dish.
    # ingredients: A list of strings representing the ingredients.

    # View All Dish Names:

    # Display a list of all the dish names in the inventory.
    # View Dish Details by Name:

    # Allow the user to input a dish name.
    # If the dish exists, display its details: name, calorie count, and ingredients.
    # If the dish does not exist, display an appropriate error message.
    # Filter Dishes by Calorie Count:

    # Provide two separate options to:
    # View all dishes below a certain calorie threshold.
    # View all dishes above a certain calorie threshold.
    # Display the name, calorie count, and ingredients for all matching dishes.
    # Add a New Dish:

    # Allow the user to input a new dish, including its name, calorie count, and ingredients (as a comma-separated list).
    # Add the new dish to the inventory.
    # Ensure that dish names are unique. If a dish with the same name already exists, prompt the user to enter a different name.
    # Remove a Dish by Name:

    # Allow the user to specify the name of a dish to remove.
    # If the dish exists, remove it from the inventory.
    # If the dish does not exist, display an appropriate error message.
    # Modify a Dish by Name:

    # Allow the user to specify a dish name to modify.
    # If the dish exists, present options to:
    # Change the dish’s name.
    # Update its calorie count.
    # Add new ingredients to the list.
    # Remove specific ingredients from the list.
    # If the dish does not exist, display an appropriate error message.
    # Search Dishes by Ingredient:

    # Allow the user to search for dishes containing a specific ingredient.
    # Display the names of all dishes that include the specified ingredient.
    # If no dishes match, display an appropriate message.
    # Exit the Program:

    # Provide an option to exit the loop and terminate the program
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
    

def read_file_put_into_dict(file_name):
    """
    Reads each line from file_name, which should look like:
    
    name: pizza calories: 500 ingrdiants: cheese,peperoni,tomato sause, bread
    
    Parses these lines into a list of dictionaries like:
    {
        "name": "pizza",
        "calories": 500,
        "ingredients": ["cheese", "peperoni", "tomato sause", "bread"]
    }
    
    Returns that list.
    """

    dish_name = ""
    calories = 0
    
    ingredients = []
    full_list = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
        # this code turns the line into two lists, one with what was on the left of ingredaints: 
        # and one with what was on the right wich should leave
        # all the ingrediants in a list but are still all one index due to ","
            try:
                name_and_cals_split, ingredients = line.split("ingredients:")
            except ValueError:
                print(f"no ingrediants found on line {line}")
                continue #no idea why this isnt working

            # finish dealing with the ingrediants by splitting at the ","
            ingredients = ingredients.split(",")
            ingredients = [ingrediant.strip() for ingrediant in ingredients] # turned into a string for some reason

            #had a parse error so doing this before stops it
            name_and_cals_split = name_and_cals_split.strip()

            try:
                name_split, calories = name_and_cals_split.split("calories:")
            except ValueError:
                print(f"no calories found on line {line}")
                continue

            calories = calories.strip()

            if is_digit(calories):
                calories = int(calories)
            else:
                print(f"calories {calories} is not a valid number")
                continue

            name_split = name_split.strip()

            try:
                trash, dish_name = name_split.split("name:")
            except ValueError:
                print(f"no name found on line {line}")
                continue
            
            dish_name = dish_name.strip()

            dish = {
                "name" : dish_name,
                "calories": calories,
                "ingredients": ingredients
            }

            full_list.append(dish)
           
    return full_list


def gets_list_of_dishes():
    while True:
        print("what is the name of the file you would like to open?")
        file_name = input()
        if file_exists(file_name):
            break
        else:
            print("this file does not exist")
            print("please try again")
    
    dishes = []
    dishes = read_file_put_into_dict(file_name)
    return dishes

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

def print_dish_details(dish):
    print(f"name: {dish['name']}, calories: {dish['calories']}, ingredients: {dish['ingredients']}")


def view_dish_details(dishes):
    while True:
        print("what dish would you like to know more about?")
        dish_name = input().lower()
        if check_dish_exists(dishes, dish_name):
            dish_index = get_dish_index(dishes, dish_name)
            break
        print("this dish does not exist in the current menu")
        print("please try again")

    print("here is additional information about the dish")
    print_dish_details(dishes[dish_index])



def filter_dishes_above(dishes, min_cals):
    # returns a list of dishes that are above the min calories
    output = []
    for dish in dishes:
        if dish['calories'] >= min_cals:
            output.append(dish)
    return output



def filter_dishes_below(dishes, max_calories):
    # returns a list of dishes that are below the max calories
    output = []
    for dish in dishes:
        if dish['calories'] >= max_calories:
            output.append(dish)
    return output


def print_dishes_below_certain_calories(dishes):
    """ responsible for asking user what calorie threshold they want to see dishes above"""
     # first, get their threshold
    while True:
        print("what is the minimum calorie count?")
        min_calories = input()
        if is_digit(min_calories):
            min_calories = int(min_calories)
            if min_calories <= 0:
                print('you have to enter a positive value')
            else:
                break
        else:
            print("please enter a valid number")

    # we know that they entered a good number
    # get the dishes:
    candidate_dishes = filter_dishes_above(dishes, min_calories)
    if (len(candidate_dishes) == 0):
        print("there are no dishes matching that calorie requirements!")
    else:
        for dish in candidate_dishes:
            print_dish_details(dish)


def print_dishes_above_certain_calories(dishes):
    """ responsible for asking user what calorie threshold they want to see dishes above"""
    # first, get their threshold
    while True:
        print("what is the minimum calorie count?")
        min_calories = input()
        if is_digit(min_calories):
            min_calories = int(min_calories)
            if min_calories <= 0:
                print('you have to enter a positive value')
            else:
                break
        else:
            print("please enter a valid number")

    # we know that they entered a good number
    # get the dishes:
    candidate_dishes = filter_dishes_above(dishes, min_calories)
    if (len(candidate_dishes) == 0):
        print("there are no dishes matching that calorie requirements!")
    else:
        for dish in candidate_dishes:
            print_dish_details(dish)

def choose_above_or_below(dishes):
    """
    the user has chosen to see dishes either above or below a certain number of calories.
    we have to decide which one it is  hter
    """
    while True:
        print("would you like to see dishes above or below a certain calorie count?")
        print("1. below")
        print("2. above")
        choice = input()
        if choice != "1" and choice !="2":
            print("that is an invalid choice. you have to pick either above or below")
        else:
            break

    if choice == 1:
        print_dishes_below_certain_calories(dishes)
    else:
        print_dishes_above_certain_calories(dishes)


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


def filter_dishes_by_ingredient(dishes, ingredient):
    # without printing anything, this function returns a list of dishes that
    # contain a certain ingredient
    output = []
    for dish in dishes:
        if ingredient in dish.get('ingredients'):
            output.append(dish)    
    return output

def search_dishes_by_ingredient(dishes):
    # print("what ingredient would you like to search for?")
    # ingredient = input().lower()
    # no_dish_found = True
    # for dish in dishes:
    #     if ingredient in dish["ingredients"]:
    #         no_dish_found = False
    #         print(dish["name"])
    # if (no_dish_found):
    #     print("there are no dishes that contain this ingredient")
    print("what ingredient would you like to search for?")
    ingredient = input().lower()
    matching_dishes = filter_dishes_by_ingredient(dishes, ingredient)
    if (len(matching_dishes) == 0):
        print("there are no dishes that contain this ingredient")
        return
    # if we got to this line it means that we actually have some dishes


    
def main():

    dishes = gets_list_of_dishes()

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