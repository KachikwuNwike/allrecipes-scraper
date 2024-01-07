from helperfunctions import get_directions, get_json, get_time


class Recipe:
    def __init__(self, soup):
        self.soup = soup
        self.data = get_json(soup)[0]
        self.name = self.data.get("name")
        self.url = None
        self.category = self.data.get("recipeCategory")
        self.get_description()
        self.get_nutrition()
        self.ingredients = self.data.get("recipeIngredient")

        self.directions = get_directions(self.data.get("recipeInstructions"))
        self.author = None

        self.servings = self.data.get("recipeYield")[0]
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

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "cuisine": self.cuisine,
            "category": self.category,
            "description": self.description,
            "nutrition_facts": self.nutrition,
            "direction": self.directions,
            "ingredients": self.ingredients,
            "author": self.author,
            "servings": self.servings,
            "prep_time": self.prep_time,
            "cook_time": self.cook_time,
            "total_time": self.total_time,
            "image_link": self.image,
            "video_link": self.video,
        }

    def __str__(self):
        return (
            f"Recipe name = {self.name}\n"
            f"Cuisine = {self.cuisine}\n"
            f"Category = {self.category}\n"
            f"Description = {self.description}\n"
            f"Nutrition = {self.nutrition}\n"
            f"Directions = {self.directions}\n"
            f"Ingredients = {self.ingredients}\n"
            f"Author = {self.author}\n"
            f"Servings = {self.servings}\n"
            f"Prep Time = {self.prep_time}\n"
            f"Cook Time = {self.cook_time}\n"
            f"Total Time = {self.total_time}\n"
            f"Image URL= {self.image}\n"
            f"Video URL= {self.video}"
        )
