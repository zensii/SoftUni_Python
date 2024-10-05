def cookbook(*recipes):
    cuisines = {}
    for recipe in recipes:
        recipe_name, cuisine, ingredients = recipe
        cuisines.setdefault(cuisine, []).append([recipe_name, ingredients])

    sorted_ingredients = dict([key, sorted(value, key= lambda x: x[0])] for key, value in cuisines.items())
    sorted_cuisines = dict(sorted(sorted_ingredients.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''

    for cuisine, cuisine_recipes in sorted_cuisines.items():
        result += f"{cuisine} cuisine contains {len(cuisine_recipes)} recipes:\n"
        for cuisine_recipe in cuisine_recipes:
            result += f"  * {cuisine_recipe[0]} -> Ingredients: {', '.join(cuisine_recipe[1])}\n"

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

