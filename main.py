import json

import requests
from bs4 import BeautifulSoup

from classes.recipe import Recipe
from helperfunctions import get_region_and_links

all_recipes = []
region_links = get_region_and_links()

for links in region_links:
    cuisine = links[0]
    for link in links[2]:
        recipes_source = requests.get(link).text
        soup = BeautifulSoup(recipes_source, "lxml")
        recipe = Recipe(soup)
        recipe.url = link
        recipe.author = "allrecipes"
        recipe.cuisine = cuisine
        recipe.name = recipe.name.replace("&#39;", "'")
        recipe_dict = recipe.to_dict()
        all_recipes.append(recipe_dict)

json_file_path = "allrecipe.json"
with open(json_file_path, "w") as json_file:
    json.dump(all_recipes, json_file, indent=2)
