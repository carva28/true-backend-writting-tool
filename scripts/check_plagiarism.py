from nltk.tokenize import sent_tokenize
from googlesearch import search
from bs4 import BeautifulSoup
import jellyfish
import cloudscraper

class PlagiarismResult:
    def __init__(self, url, ratio, sentence):
        self.url = url
        self.ratio = ratio
        self.sentence = sentence

    def to_dict(self):
        return {
            "url": self.url, 
            "ratio": self.ratio, 
            "sentence": self.sentence}

scraper = cloudscraper.create_scraper()

def check_plagirism(input):
    tokenized_text = split_text(input)
    response = []

    for sentence in tokenized_text:
        google_results = search(sentence, tld="pt", num=1, stop=1, pause=2)

        for url in google_results:
            res = scraper.get(url)
            html_page = res.content
            html_parse = BeautifulSoup(html_page, 'html.parser')

            # getting all the paragraphs
            for paragraph in html_parse.find_all("p"):
                text = BeautifulSoup.get_text(paragraph)
                ratio = jaro_distance(text, sentence)
                
                if ratio > 0.8:
                    response.append(PlagiarismResult(url, ratio, text))

    results = [obj.to_dict() for obj in response]
    return results

def split_text(text):
    return sent_tokenize(text)

def jaro_distance(a, b):
    return jellyfish.jaro_similarity(str(a), str(b))
