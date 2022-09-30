import json
from nltk.corpus import wordnet as wn
from .list_cleaner import *
from .remove_plural import remove_plural_words

max_response_lenght = 3

def procurarSinonimos(palavra):

    item = {
        'word': clean_special_chars(palavra.lower()), 
        'isUpper': is_upper_case(palavra), 
        'startSpace': starts_with_space(palavra), 
        'endSpace': ends_with_space(palavra)
        }

    palavrasSugeridas = []
    syns = wn.synsets(item['word'], lang='por')


    for syn in syns:
        for lem in syn.lemmas(lang='por'):
            name = lem.name()
            name = name.replace("_", " ")
            palavrasSugeridas.append(name.lower())

    # filtrar sugestões
    filteredList = remove_duplicates(palavrasSugeridas)
    filteredList = remove_list_item(filteredList, item['word'])
    filteredList = remove_plural_words(filteredList, item['word'])
    filteredList = filteredList[:max_response_lenght]

    if item['isUpper']:
        filteredList = [e.capitalize() for e in filteredList]

    if item['startSpace']:
        filteredList = [" " + e for e in filteredList]

    if item['endSpace']:
        filteredList = [e + " " for e in filteredList]

    print("filtered: ", filteredList)

    return json.loads(json.dumps(filteredList))

#procurarSinonimos('assim')
