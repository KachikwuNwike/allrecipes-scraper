This project is a web scraper designed to extract recipe information, including cuisine details, from "https://www.allrecipes.com/cuisine-a-z-6740455". The scraper is built in Python and organized into three files:

- recipe.py: Defines a Recipe class with attributes representing various details of a recipe.
- links.py: Contains a function get_region_and_links() that retrieves a list of cuisines and their corresponding recipe links.
- allrecipe.py: The main file that orchestrates the scraping process, iterates through the links, and collects recipe data using the Recipe class. The final output is stored in an Excel file named "allrecipe.xlsx."

Files
"recipe.py"
This file defines the Recipe class, which encapsulates the structure of recipe data.

"links.py"
This file contains the function get_region_and_links(), which retrieves a list of cuisines along with their corresponding recipe links. The links are used in the main scraping process.

"allrecipe.py"
The main file that drives the scraping process. It obtains the list of links using get_region_and_links() and, for each link, scrapes the webpage using the Recipe class. The final output is stored in "allrecipe.xlsx."