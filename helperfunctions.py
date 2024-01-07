import json
from datetime import timedelta

import requests
from bs4 import BeautifulSoup


def get_json(soup):
    data = soup.find("script", type="application/ld+json").contents
    return json.loads("".join(data))


def get_directions(steps):
    directions = {}
    step_number = 0
    for step in steps:
        if step.get("@type") == "HowToStep":
            step_number += 1
            directions[str(step_number)] = step.get("text")
    return directions


def get_time(time):
    if time is not None:
        time = int(time[2:-1])
        time = str(timedelta(minutes=time))
        return time


def get_region_and_links():
    recipes_source = requests.get("https://www.allrecipes.com/cuisine-a-z-6740455").text

    soup = BeautifulSoup(recipes_source, "lxml")

    cuisines_soup = soup.find_all(
        "a", class_="link-list__link type--dog-bold type--dog-link"
    )

    region_links = []
    for cuisine in cuisines_soup:
        cuisine_name = cuisine.text.strip()
        cuisine_link = cuisine["href"]

        region_links.append([cuisine_name, cuisine_link])

    for index, region in enumerate(region_links):
        link = region[1]
        recipes_source = requests.get(link).text

        soup = BeautifulSoup(recipes_source, "lxml")
        data = get_json(soup)
        temp = data[0].get("itemListElement")
        links = []
        for x in temp:
            valid = x.get("url")
            if (
                "gallery" not in valid
                and "article" not in valid
                and "-vs-" not in valid
                and "what-is-" not in valid
                and "substitute" not in valid
                and "nowruz" not in valid
                and "foods-in-every" not in valid
                and "longform" not in valid
            ):
                links.append(valid)
        region_links[index].append(links)

    return region_links
