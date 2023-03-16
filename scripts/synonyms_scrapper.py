import requests
from bs4 import BeautifulSoup
from .list_cleaner import *
import cloudscraper

baseURL = "https://www.infopedia.pt/dicionarios/lingua-portuguesa/"
divId = "relacoesSinonimosContainer"
max_response_lenght = 7
scraper = cloudscraper.create_scraper()

def scrap_synonyms(word):

    item = {
        'isUpper': is_upper_case(word), 
        'startSpace': starts_with_space(word), 
        'endSpace': ends_with_space(word)
    }

    synonymsList = []
    
    res = scraper.get(baseURL + word)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    synonyms_container = soup.find(id = divId)

    if synonyms_container == None:
        print("cant find container")
        return synonymsList

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

    # print(synonymsList)

    return synonymsList
 