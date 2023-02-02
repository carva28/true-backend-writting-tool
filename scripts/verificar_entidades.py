import spacy
from spacy.lang.pt.examples import sentences 
import pandas as pd
from spacy import displacy
from spacy.tokens import DocBin
from spacy import displacy
import json

nlp = spacy.load("pt_core_news_sm")

# ruler = nlp.add_pipe("entity_ruler", before="ner")


def encontrarEntidades(texto):

    doc = nlp(texto)

    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

    # entidades_pesquisadas = []

    # doc = nlp(texto)
    # for ent in doc.ents:
    #     entidades_pesquisadas.append({'entidade': ent.text, 'label': ent.label_})

    # json_string = json.loads(json.dumps(entidades_pesquisadas)) 
     
    # print(entidades_pesquisadas)
    # return json_string
    # doc = nlp(texto)

    # print(doc.text)

    # for token in doc:
    #     print(token.text, token.pos_, token.dep_)


text = "Este fim de semana a nossa escola participou no torneio nacional de futebol e conquistou o 1º lugar. Todos os participantes estão de parabéns."
encontrarEntidades(text)