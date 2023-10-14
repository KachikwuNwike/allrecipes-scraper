import requests
from bs4 import BeautifulSoup

from getjson import get_json


def get_region_and_links():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
    }

    recipes_source = requests.get(
        "https://www.allrecipes.com/cuisine-a-z-6740455",
        headers=headers,
    ).text

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
        recipes_source = requests.get(
            link,
            headers=headers,
        ).text

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
