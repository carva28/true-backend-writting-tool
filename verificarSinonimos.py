import enchant
from enchant.checker import SpellChecker
from enchant.checker.CmdLineChecker import CmdLineChecker
from collections import defaultdict
import json
import re
from nltk.corpus import wordnet as wn

my_dict = enchant.DictWithPWL("pt_PT", "palavras.txt")
#chkr = SpellChecker("pt_PT","palavras.txt")
chkr = SpellChecker(my_dict)

def remove(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)

def procurarSinonimos(palavra):
    palavra_Corrigir = ""

    removerTagHtml = remove(palavra)


    op1 = ''.join(e for e in palavra if e.isalpha())

    print("test filtro", op1)

    palavra_Corrigir = op1
    palavrasSugeridas = []
    arrayTexto = op1.split()
    syns = wn.synsets(palavra_Corrigir, lang='por')
    for syn in syns:
        for lem in syn.lemmas(lang='por'):
            name = lem.name()
            palavrasSugeridas.append(name)
            print(name)


    #chkr.set_text(palavra_Corrigir)

    #palavrasSugeridas = chkr.suggest(palavra_Corrigir)

    
    json_palavrasSugeridas = json.loads(json.dumps(palavrasSugeridas)) 
        
    print(palavrasSugeridas)

    return json_palavrasSugeridas


#procurarSinonimos('cão. %&/%#')


# Verificar palavras repetidas / duplicados, se a letra da palavra começa por maiuscula ou minuscula, plurais / Saber que a palavra vem com espaços e enviar com espaço/maisucula e minuscula