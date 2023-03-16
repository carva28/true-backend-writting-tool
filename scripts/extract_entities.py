import spacy

nlp = spacy.load("pt_core_news_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        entities.append(ent.text)
        
    print(entities)  

    return entities
    