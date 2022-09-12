import enchant
from enchant.checker import SpellChecker
import json
import re
from re import search
import numpy as np
from pandas import *
import pandas as pd

my_dict = enchant.Dict("pt_PT")
chkr = SpellChecker(my_dict)
pos_repeated_clean = []
pos_repeated_clean_v2 = []

#Limpar Bolds, Italics... Tags
def remove(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)

#Detetar a Posicao das Palavras Erradas
def verificarPosPalavras(palavraDescoPos, textoCompletoComparar, posARR):
    global pos_repeated_clean
    if posARR == 0:
        pos_repeated_clean = []
    else:
        pos_repeated_clean = pos_repeated_clean 
       
    for match in re.finditer(r'\b%s\b' % palavraDescoPos, textoCompletoComparar):
                clean_arr_data = []
                
                pos_ini = int(match.start())
                
                pos_repeated_clean.append([pos_ini,match.group(),match.start(),match.end()])

                #Ordenar o array pela posicao inicial
                pos_repeated_clean.sort()

                #Evitar valores repetidos sobre a posicao das palavras
                unique_values = np.array(pos_repeated_clean)
                clean_arr_data = DataFrame(unique_values).drop_duplicates().values
    
    #print(clean_arr_data)
        
    return clean_arr_data

#Detetar a Posicao das Palavras Certas para enviar para o Front-End e pintar de preto
def verificarPosPalavrasCorretas(palavraDescoPos, textoCompletoComparar, posARR):
    global pos_repeated_clean_v2
    global clean_arr_data_2

    if posARR == 0:
        pos_repeated_clean_v2 = []
    else:
        pos_repeated_clean_v2 = pos_repeated_clean_v2 
        #print("whats is the values:",  pos_repeated_clean )

    for match in re.finditer(r'\b%s\b' % palavraDescoPos, textoCompletoComparar):
                clean_arr_data_2 = []
                
                #print("match", count, match.group(), "start index", match.start(), "End index", match.end())
                pos_ini = int(match.start())
                
                pos_repeated_clean_v2.append([pos_ini,match.group(),match.start(),match.end()])

                #Ordenar o array pela posicao inicial
                pos_repeated_clean_v2.sort()

                #Evitar valores repetidos sobre a posicao das palavras
                unique_values_v2 = np.array(pos_repeated_clean_v2)
                clean_arr_data_2 = DataFrame(unique_values_v2).drop_duplicates().values
    return clean_arr_data_2

def recebeTextoParaDetetar(texto):


    textoAcorrigir = ""
    palavras_POS = ""
    palavras_POS_corretas = ""
    posicaoPalavras_Errada = pd.DataFrame(None).to_json(orient='split',force_ascii=False)
    posicaoPalavras_Corretas = pd.DataFrame(None).to_json(orient='split',force_ascii=False)
    removerTagHtml = remove(texto)

    #Limpar caracteres especial
    special_char_list = ["&nbsp;","$",'"',"@", "#", "&", "%",".",",","*","**","(",")","'",'"',"`","´",'<','>','{','}','=>','})','})}','}>',"<button type='button' class='btn_sinonimos' >","</button>", ]
    # using list comprehension
    op1 = "".join([k for k in removerTagHtml if k not in special_char_list])
    #print(f"op1 = ", op1)

    textoAcorrigir = op1
    arrayTexto = op1.split()

    #O checker irá verificar os erros no texto que vem do front-end
    chkr.set_text(textoAcorrigir)

    palavrasSugeridas = {}
    arrayTotal_do_texto_escrito_set = []
    palavrasErradas = []

    #Regex para detetar se uma palavra tem hífen
    p = re.compile("(?=\S*['-])([a-zA-Z'-]+)")
    
    for err in chkr:
        #Correção que sugere para a palavra com erro
        sug = err.suggest()

        print(sug)

        #Ciclo para encontra as sugestões com hífen
        palavraComHifen = [ s for s in sug if p.match(s) ]

        #Se tiver hífen então acrescenta essa opção em primeiro lugar
        if len(palavraComHifen) != 0:
            sug.remove(palavraComHifen[0])
            sug.insert(0,palavraComHifen[0])
        
        #Identificar qual é a palavra errada
        palavraMa = err.word

        if (len(palavraMa) == 1):
            print(True)
        else:
            #Guardar a lista de palavras sugeridas para a correção
            palavrasSugeridas.setdefault(err.word, []).append(sug)
          
            palavrasErradas.append(err.word)
   
    palavr_Arra_Origin_Count = []
    contarPalavvras = 0

    for quantasPalavrasOriginais in arrayTexto:
        #print(quantasPalavrasOriginais, contarPalavvras);
        palavr_Arra_Origin_Count.append([quantasPalavrasOriginais,contarPalavvras])
        contarPalavvras = contarPalavvras + 1
        
    a = palavr_Arra_Origin_Count
    colocarPalavrasBemMal = []
    arrayTexto_pos_erros = []
    palavras_POS = ""
    palavras_POS_corretas = ""
    primeiraWord = 0
    for count in a:

        if count[0] in palavrasErradas:
            colocarPalavrasBemMal.append([count[0],count[1],"errada"])
            arrayTexto.remove(count[0])
            posARR = palavrasErradas.index(count[0])
            palavras_POS = verificarPosPalavras(count[0], textoAcorrigir, posARR)
           
        else:
            #arrayTexto.replace(count[0],[count[0],count[1]])
            if (primeiraWord == 0):

                colocarPalavrasBemMal.append([count[0],count[1],"certa"])
                arrayTexto_pos_erros.append(count[1]) 
            
                posARR_v2 = 0   
                palavras_POS_corretas = verificarPosPalavrasCorretas(count[0], textoAcorrigir, posARR_v2)
                primeiraWord = primeiraWord + 1
            else:
                colocarPalavrasBemMal.append([count[0],count[1],"certa"])
                arrayTexto_pos_erros.append(count[1]) 
            
                posARR_v2 = count[1]   
                palavras_POS_corretas = verificarPosPalavrasCorretas(count[0], textoAcorrigir, posARR_v2)

    count = 0

    arrayTotal_do_texto_escrito_set = set(arrayTexto)
    palavrasErradas_v2 = set(palavrasErradas)

    matches = arrayTotal_do_texto_escrito_set.symmetric_difference(palavrasErradas_v2)
    json_solve_array = list(matches)
    palavraRecomendadasParaCorrecao = json.loads(json.dumps(palavrasSugeridas)) 
    array_de_palavras_Mal = json.loads(json.dumps(palavrasErradas)) 
    links_Sinonimo = json.loads(json.dumps(json_solve_array)) 
    lista_palavrasBemMal = json.loads(json.dumps(colocarPalavrasBemMal))

    #Preparar a lista de posições das palavras erradas e corretas para um JSON
    if len(palavras_POS) > 0:
        posicaoPalavras_Errada =  pd.DataFrame(columns=palavras_POS).to_json(orient='split',force_ascii=False)
    else:
        posicaoPalavras_Errada = pd.DataFrame(columns=["nothing"]).to_json(orient='split',force_ascii=False)

    if len(palavras_POS_corretas) > 0:
        posicaoPalavras_Corretas =  pd.DataFrame(columns=palavras_POS_corretas).to_json(orient='split',force_ascii=False)
    else:
        posicaoPalavras_Corretas =  pd.DataFrame(columns=["nothing"]).to_json(orient='split',force_ascii=False)

    return palavraRecomendadasParaCorrecao,array_de_palavras_Mal,links_Sinonimo,lista_palavrasBemMal,posicaoPalavras_Errada,posicaoPalavras_Corretas

recebeTextoParaDetetar('Caramulo')
