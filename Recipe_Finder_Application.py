
recipes = [
    {"name": "Pancakes", "ingredients": ["flour", "milk", "egg"], "type": "Breakfast"},
    {"name": "Chicken Salad", "ingredients": ["chicken", "lettuce", "tomato"], "type": "Lunch"},
    {"name": "White Sauce Pasta", "ingredients": ["pasta", "tomato sauce", "cheese"], "type": "Dinner"},
]

def search_recipes():
    ingredients = input("Enter ingredients (comma-separated): ").lower().split(",")
    ingredients = [item.strip() for item in ingredients]
    print("\nMatching Recipes:")
    for recipe in recipes:
        if all(ingredient in recipe["ingredients"] for ingredient in ingredients):
            print(f"- {recipe['name']} ({recipe['type']})")
    print()

def filter_recipes_by_type():
    recipe_type = input("Enter recipe type (Breakfast, Lunch, Dinner): ").capitalize()
    print("\nRecipes:")
    for recipe in recipes:
        if recipe["type"] == recipe_type:
            print(f"- {recipe['name']}")
    print()

def main():
    while True:
        print("1. Search Recipes")
        print("2. Filter Recipes by Type")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            search_recipes()
        elif choice == "2":
            filter_recipes_by_type()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
