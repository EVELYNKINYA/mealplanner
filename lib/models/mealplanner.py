# mealplanner.py

class MealPlanner:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def display_meals(self):
        for idx, meal in enumerate(self.meals, start=1):
            print(f"{idx}. {meal}")

# To add methods to add, delete and display meal plans here