import json
from datetime import timedelta


def get_json(soup):
    data = soup.find("script", type="application/ld+json").contents
    return json.loads("".join(data))[0]


def get_directions(steps):
    directions = []
    for step in steps:
        if step.get("@type") == "HowToStep":
            directions.append(step.get("text"))
            image = step.get("image")
            if image:
                image = image[0]
                image = image.get("url")

    directions.append(image)
    return directions


def get_time(time):
    if time is not None:
        time = int(time[2:-1])
        time = str(timedelta(minutes=time))
        return time


class Recipe:
    def __init__(self, soup):
        self.soup = soup
        self.data = get_json(soup)
        self.name = self.data.get("name")
        self.category = self.data.get("recipeCategory")
        self.get_description()
        self.get_nutrition()
        self.ingredients = self.data.get("recipeIngredient")

        self.directions = get_directions(self.data.get("recipeInstructions"))[:-1]

        try:
            self.author = self.data.get("author")[0].get("name")
        except:
            self.author = None

        self.servings = self.data.get("recipeYield")
        self.get_image()
        self.get_video()
        self.cuisine = None

        self.prep_time = get_time(self.data.get("prepTime"))
        self.cook_time = get_time(self.data.get("cookTime"))
        self.total_time = get_time(self.data.get("totalTime"))

    def get_description(self):
        self.description = (
            self.data.get("description")
            .replace("&amp;mdash;", "—")
            .replace("&mdash;", "—")
        )

    def get_nutrition(self):
        self.nutrition = self.data.get("nutrition")
        if self.nutrition is not None:
            del self.nutrition[list(self.nutrition.keys())[0]]

    def get_image(self):
        try:
            self.image = self.data.get("image").get("url")
        except:
            self.image = None

    def get_video(self):
        try:
            self.video = self.data.get("video").get("contentUrl")
        except:
            self.video = None

    def __str__(self):
        x = f"Recipe name = {self.name}\nCuisine = {self.cuisine}\nCategory = {self.category}\nDescription = {self.description}\nNutrition = {self.nutrition}\nDirections = {self.directions}\nIngredients = {self.ingredients}\nAuthor = {self.author}"
        y = f"\nServings = {self.servings}\nPrep Time = {self.prep_time}\nCook Time = {self.cook_time}\nTotal Time = {self.total_time}\nImage URL= {self.image}\nVideo URL= {self.video}"
        return x + y
