```python
/*
Author: Durgesh Mahajan
Date: 2023-10-05 10:30:00
Project: Home Chef Helper Command-Line Application
*/

import json
import os

# Constants
RECIPE_FILE = 'recipes.json'

# Function to load recipes from a JSON file
def load_recipes():
    if os.path.exists(RECIPE_FILE):
        with open(RECIPE_FILE, 'r') as file:
            recipes = json.load(file)
    else:
        recipes = []
    return recipes

# Function to save recipes to a JSON file
def save_recipes(recipes):
    with open(RECIPE_FILE, 'w') as file:
        json.dump(recipes, file, indent=4)

# Function to add a new recipe
def add_recipe(recipes):
    name = input("Enter recipe name: ").strip()
    if any(recipe['name'].lower() == name.lower() for recipe in recipes):
        print(f"A recipe named '{name}' already exists.")
        update = input("Do you want to update the existing recipe? (yes/no): ").strip().lower() == 'yes'
        if update:
            edit_recipe(recipes, name)
        return

    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or type 'done' to finish): ").strip()
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)

    instructions = input("Enter preparation instructions: ").strip()
    prep_time = int(input("Enter estimated prep time (in minutes): "))
    cook_time = int(input("Enter cook time (in minutes): "))
    category = input("Enter category (e.g., Breakfast, Dinner, Dessert): ").strip()

    recipe = {
        'name': name,
        'ingredients': ingredients,
        'instructions': instructions,
        'prep_time': prep_time,
        'cook_time': cook_time,
        'category': category
    }
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")

# Function to view all recipes
def view_recipes(recipes):
    if not recipes:
        print("No recipes available.")
        return
    for idx, recipe in enumerate(recipes, start=1):
        print(f"{idx}. {recipe['name']}")
    
    try:
        choice = int(input("Enter the number of the recipe to view full details (or 0 to go back): "))
        if choice == 0:
            return
        elif 1 <= choice <= len(recipes):
            recipe = recipes[choice - 1]
            print(f"\nName: {recipe['name']}")
            print(f"Category: {recipe['category']}")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}")
            print(f"Preparation Time: {recipe['prep_time']} minutes")
            print(f"Cooking Time: {recipe['cook_time']} minutes")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to search recipes
def search_recipes(recipes):
    if not recipes:
        print("No recipes available.")
        return
    search_term = input("Enter search term (recipe name or ingredient): ").strip().lower()
    results = [recipe for recipe in recipes if search_term in recipe['name'].lower() or
                                            any(search_term in ingredient.lower() for ingredient in recipe['ingredients'])]
    if not results:
        print("No matching recipes found.")
        return
    for idx, recipe in enumerate(results, start=1):
        print(f"{idx}. {recipe['name']}")
    print("End of search results.")

# Function to edit a recipe
def edit_recipe(recipes, name=None):
    if not name:
        view_recipes(recipes)
        try:
            choice = int(input("Enter the number of the recipe to edit (or 0 to go back): "))
            if choice == 0:
                return
            elif 1 <= choice <= len(recipes):
                recipe = recipes[choice - 1]
            else:
                print("Invalid choice. Please try again.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    else:
        recipe = next((r for r in recipes if r['name'].lower() == name.lower()), None)
        if not recipe:
            print(f"No recipe found with name '{name}'.")
            return

    print(f"Editing recipe: {recipe['name']}")
    recipe['name'] = input(f"Enter new name (current: {recipe['name']}): ") or recipe['name']
    recipe['ingredients'] = []
    while True:
        ingredient = input("Enter an ingredient (or type 'done' to finish, 'keep' to retain current): ").strip()
        if ingredient.lower() == 'done':
            break
        elif ingredient.lower() == 'keep':
            recipe['ingredients'] = recipe.get('ingredients', [])
            break
        else:
            recipe['ingredients'].append(ingredient)

    recipe['instructions'] = input(f"Enter new preparation instructions (current: {recipe['instructions']}): ") or recipe['instructions']
    recipe['prep_time'] = int(input(f"Enter new preparation time (in minutes, current: {recipe['prep_time']}): ") or recipe['prep_time'])
    recipe['cook_time'] = int(input(f"Enter new cook time (in minutes, current: {recipe['cook_time']}): ") or recipe['cook_time'])
    recipe['category'] = input(f"Enter new category (current: {recipe['category']}): ") or recipe['category']

    save_recipes(recipes)
    print("Recipe updated successfully!")

# Function to delete a recipe
def delete_recipe(recipes):
    if not recipes:
        print("No recipes available.")
        return
    view_recipes(recipes)
    try:
        choice = int(input("Enter the number of the recipe to delete (or 0 to go back): "))
        if choice == 0:
            return
        elif 1 <= choice <= len(recipes):
            recipe = recipes.pop(choice - 1)
            print(f"Recipe '{recipe['name']}' deleted successfully!")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    save_recipes(recipes)

# Main menu function
def main_menu():
    recipes = load_recipes()
    while True:
        print("\nHome Chef Helper - Recipe Manager")
        print("1. Add New Recipe")
        print("2. View All Recipes")
        print("3. Search Recipes")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_recipe(recipes)
            elif choice == 2:
                view_recipes(recipes)
            elif choice == 3:
                search_recipes(recipes)
            elif choice == 4:
                edit_recipe(recipes)
            elif choice == 5:
                delete_recipe(recipes)
            elif choice == 6:
                save_recipes(recipes)
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
```

This program provides a command-line interface for managing recipes with functionalities to add, view, search, edit, and delete recipes. All recipes are stored persistently in a JSON file named `recipes.json`. 

### Key Features:
- **Modular Design:** The program is organized into functions, each handling a specific task.
- **User Experience:** The interface is simple and clear, with intuitive prompts and clear output.
- **Error Handling:** The program performs basic input validation and handles unexpected input gracefully.
- **Data Persistence:** Recipes are saved to and loaded from a JSON file, ensuring persistence across sessions.

### Instructions:
1. Save the code in a file, for example, `home_chef_helper.py`.
2. Run the program using a Python interpreter (e.g., `python home_chef_helper.py`).
3. Use the menu options to manage your recipes.