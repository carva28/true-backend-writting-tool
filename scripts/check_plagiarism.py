from nltk.tokenize import sent_tokenize
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import jellyfish
import cloudscraper

class PlagerismResult:
    def __init__(self, url, ratio, sentence):
        self.url = url
        self.ratio = ratio
        self.sentence = sentence

    def to_dict(self):
        return {
            "url": self.url, 
            "ratio": self.ratio, 
            "sentence": self.sentence}

def checkPlagirism(input):
    print("input: ---- ", input)
    tokenizedText = splitText(input)
    response = []
    scraper = cloudscraper.create_scraper()

    for sentence in tokenizedText:
        googleResults = search(sentence, tld="pt", num=10, stop=3, pause=2)

        for url in googleResults:
            res = scraper.get(url)
            html_page = res.content
            htmlParse = BeautifulSoup(html_page, 'html.parser')

            # getting all the paragraphs
            for paragraph in htmlParse.find_all("p"):
                text = BeautifulSoup.get_text(paragraph)
                ratio = jaro_distance(text, sentence)

                if(ratio > 0.8):
                    response.append(PlagerismResult(url, ratio, text))

    results = [obj.to_dict() for obj in response]
    return results

def splitText(text):
    return sent_tokenize(text)

def jaro_distance(a, b):
    return jellyfish.jaro_similarity(str(a), str(b))
