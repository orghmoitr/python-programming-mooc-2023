# Write your solution here

def read_recipes(filename: str) -> list:
    temp_list = [""]
    with open(filename) as recipe_file:
        for line in recipe_file:
            temp_list.append(line.strip())
            
    recipes = []
    for i in range(len(temp_list)):
        recipe = {}
        if temp_list[i] == "":
            recipe["name"] = temp_list[i+1]
            recipe["cooking_time"] = int(temp_list[i+2])
            ingredients = []
            for j in range(i+3, len(temp_list)):
                if temp_list[j] == "":
                    break
                ingredients.append(temp_list[j])
            recipe["ingredients"] = ingredients
            recipes.append(recipe)

    return recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipe_names = []
    for recipe in read_recipes(filename):
        if ingredient in recipe["ingredients"]:
            recipe_names.append(f"{recipe['name']}, preparation time {recipe['cooking_time']} min")
    return recipe_names

def search_by_time(filename: str, prep_time: int) -> list:
    recipe_names = []
    for recipe in read_recipes(filename):
        if recipe["cooking_time"] <= prep_time:
            recipe_names.append(f"{recipe['name']}, preparation time {recipe['cooking_time']} min")
    return recipe_names

def search_by_name(filename: str, word: str) -> list:
    recipe_names = []
    for recipe in read_recipes(filename):
        if word.lower() in recipe["name"].lower():
            recipe_names.append(recipe["name"])
    return recipe_names

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")
# for recipe in found_recipes:
#     print(recipe)
