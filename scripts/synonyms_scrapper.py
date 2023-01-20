import requests
import json
from bs4 import BeautifulSoup
from .list_cleaner import *

baseURL = "https://www.infopedia.pt/dicionarios/lingua-portuguesa/"
divId = "relacoesSinonimosContainer"
max_response_lenght = 4

def scrap_synonyms(word):

    item = {
        'isUpper': is_upper_case(word), 
        'startSpace': starts_with_space(word), 
        'endSpace': ends_with_space(word)
    }

    synonymsList = []
    page = requests.get(baseURL + word)
    soup = BeautifulSoup(page.content, "html.parser")
    synonyms_container = soup.find(id=divId)
    results = synonyms_container.find_all("a")

    for element in results:
        synonym = element.text.strip()
        synonymsList.append(synonym)

    synonymsList = synonymsList[:max_response_lenght]

    if item['isUpper']:
        synonymsList = [e.capitalize() for e in synonymsList]

    if item['startSpace']:
        synonymsList = [" " + e for e in synonymsList]

    if item['endSpace']:
        synonymsList = [e + " " for e in synonymsList]    

    print(synonymsList)
    return json.loads(json.dumps(synonymsList))

scrap_synonyms("Guerra")