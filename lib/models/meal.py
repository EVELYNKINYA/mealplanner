
class Meal:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {', '.join(str(ing) for ing in self.ingredients)}"

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
