from nltk.tokenize import sent_tokenize
from googlesearch import search
from bs4 import BeautifulSoup
import jellyfish
import cloudscraper
import requests

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

urlUpdateNews = "https://true-project.mog-technologies.com/back-office/news/"
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyZjY2NWFjNmY4MjNkMDAxMzdkZDgwYyIsImlhdCI6MTY3NDIyNjAxMSwiZXhwIjoxNjc2ODE4MDExfQ.lgU4ZGrt8akh30TV-R_gwaE-mW27pM91J_RiFe63UWE"}

def check_plagirism(input, newsID):

    #print("newsID: ---", newsID)
    #print("input: ----", input)

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
    #print(results)
    
    endpoint = urlUpdateNews + newsID
    payload = {'plagiarized': results}
    
    r = requests.put(endpoint, json=payload, headers=headers)
    
    #print(r)
    #print(r.content)

    return results

def split_text(text):
    return sent_tokenize(text)

def jaro_distance(a, b):
    return jellyfish.jaro_similarity(str(a), str(b))
