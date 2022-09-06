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

    special_char_list = ["$", "@", "#", "&", "%","*","**","(",")","'",'"','<','>','{','}','=>','})','})}','}>',"<button type='button' onClick={function incrementHitIndex(){setCount(count + 1)}}>"]
    # using list comprehension
    op1 = "".join([k for k in removerTagHtml if k not in special_char_list])
    print(f"op1 = ", op1)


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


#procurarSinonimos('cão')


