import json


def get_json(soup):
    data = soup.find("script", type="application/ld+json").contents
    return json.loads("".join(data))
