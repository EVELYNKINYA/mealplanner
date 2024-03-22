import sqlite3
from .ingredient import Ingredient
from .meal import Meal
from .mealplanner import MealPlanner

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()


def add_meal_to_planner(planner):
    name = input("Enter meal name: ")
    num_ingredients = int(input("How many ingredients does the meal have? "))

    ingredients = []
    for _ in range(num_ingredients):
        ingredient_name = input("Enter ingredient name: ")
        quantity = input("Enter quantity: ")
        unit = input("Enter unit: ")
        ingredient = Ingredient(ingredient_name, quantity, unit)
        ingredients.append(ingredient)

    meal = Meal(name, ingredients)
    planner.add_meal(meal)
    print("Meal added to planner.")

# Example usage:
planner = MealPlanner()  
add_meal_to_planner(planner)
