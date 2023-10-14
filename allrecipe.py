import pandas as pd
import requests
from bs4 import BeautifulSoup

from links import get_region_and_links
from recipe import Recipe

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}

df = pd.DataFrame(
    columns=[
        "Recipe Name",
        "Cuisine",
        "Author",
        "Category",
        "Description",
        "Servings",
        "Nutrition Facts",
        "Ingredients",
        "Directions",
        "Prep time",
        "Cook time",
        "Total time",
        "Image Link",
        "Video Link",
    ]
)

region_links = get_region_and_links()

for links in region_links:
    cuisine = links[0]
    for link in links[2]:
        recipes_source = requests.get(link, headers=headers).text
        soup = BeautifulSoup(recipes_source, "lxml")
        allrecipes_recipe = Recipe(soup)
        allrecipes_recipe.author = "allrecipes"
        allrecipes_recipe.cuisine = cuisine
        allrecipes_recipe.name = allrecipes_recipe.name.replace("&#39;", "'")

        df.loc[len(df.index)] = [
            allrecipes_recipe.name,
            allrecipes_recipe.cuisine,
            allrecipes_recipe.author,
            allrecipes_recipe.category,
            allrecipes_recipe.description,
            allrecipes_recipe.servings,
            allrecipes_recipe.nutrition,
            allrecipes_recipe.ingredients,
            allrecipes_recipe.directions,
            allrecipes_recipe.prep_time,
            allrecipes_recipe.cook_time,
            allrecipes_recipe.total_time,
            allrecipes_recipe.image,
            allrecipes_recipe.video,
        ]

with pd.ExcelWriter("allrepice.xlsx") as writer:
    df.to_excel(writer, index=False)
