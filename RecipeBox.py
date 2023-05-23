class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeBox:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, ingredients, instructions):
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)

    def get_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                return recipe
        return None

    def get_all_recipes(self):
        return self.recipes

# Create an instance of RecipeBox
recipe_box = RecipeBox()

# Add recipes
recipe_box.add_recipe("Pancakes", ["1 cup flour", "2 tbsp sugar", "1 tsp baking powder"], "1. Mix dry ingredients. 2. Add milk and eggs. 3. Mix until smooth. 4. Cook on a griddle.")
recipe_box.add_recipe("Spaghetti Bolognese", ["1 lb ground beef", "1 onion", "2 cloves garlic"], "1. Brown ground beef. 2. Add onion and garlic. 3. Cook until fragrant. 4. Add tomatoes and simmer. 5. Serve with cooked spaghetti.")

# Get a specific recipe
recipe = recipe_box.get_recipe("Pancakes")
print("Recipe:", recipe.name)
print("Ingredients:", recipe.ingredients)
print("Instructions:", recipe.instructions)

# Get all recipes
all_recipes = recipe_box.get_all_recipes()
print("\nAll Recipes:")
for recipe in all_recipes:
    print("Recipe:", recipe.name)
    print("Ingredients:", recipe.ingredients)
    print("Instructions:", recipe.instructions)
    print("--------------------")
