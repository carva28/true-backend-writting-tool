import spacy
import pandas as pd
from spacy import displacy
from spacy.tokens import DocBin
from spacy import displacy
import json

df = pd.read_csv("data_pt.csv", sep=";")

doencas = df.Doencas.tolist()
serras = df.Serra.tolist()
desportos = df.Desporto.tolist()
comidas = df.Comida.tolist()

nlp = spacy.load("pt_core_news_sm")

ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = []

for doenca in doencas:
    patterns.append({"label": "DOENCAS", "pattern": doenca})

for serra in serras:
    patterns.append({"label": "SERRAS", "pattern": serra})

for desporto in desportos:
    patterns.append({"label": "DESPORTO", "pattern": desporto})

for comida in comidas:
    patterns.append({"label": "COMIDA", "pattern": comida})

ruler.add_patterns(patterns)

def encontrarEntidades(texto):

    entidades_pesquisadas = []

    doc = nlp(texto)
    for ent in doc.ents:
        entidades_pesquisadas.append({'entidade': ent.text, 'label': ent.label_})

    json_string = json.loads(json.dumps(entidades_pesquisadas)) 
     
    return json_string
