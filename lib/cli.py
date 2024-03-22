from models.meal import MealPlanner

def main():
    planner = MealPlanner()

    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Exiting the program...")
            break
        elif choice == "1":
            add_meal(planner)
        elif choice == "2":
            planner.display_meals()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a meal")
    print("2. View planned meals")
    print("3. Edit a planned meal")
    print("4. Delete a planned meal")


def add_meal(planner):
    print("Adding a meal to the planner...")
    name = input("Enter meal name: ")
    num_ingredients = int(input("How many ingredients does the meal have? "))

    ingredients = []
    for _ in range(num_ingredients):
        ingredient_name = input("Enter ingredient name: ")
        quantity = input("Enter quantity: ")
        unit = input("Enter unit: ")
        ingredients.append((ingredient_name, quantity, unit))

    meal = (name, ingredients)
    planner.add_meal(meal)
    print("Meal added to planner.")


if __name__ == "__main__":
    main()
