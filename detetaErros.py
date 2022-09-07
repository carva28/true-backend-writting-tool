import enchant
from enchant.checker import SpellChecker
from enchant.checker.CmdLineChecker import CmdLineChecker
from collections import defaultdict
import json,codecs
import re
from re import search
from collections import Counter
import numpy as np
from pandas import *
import pandas as pd

repeat_Var = -1

my_dict = enchant.DictWithPWL("pt_PT", "palavras.txt")
#chkr = SpellChecker("pt_PT","palavras.txt")
chkr = SpellChecker(my_dict)

pos_repeated_clean = []
pos_repeated_clean_v2 = []

#Limpar Bolds, Italics... Tags
def remove(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, ' ', text)


def verificarPosPalavras(palavraDescoPos, textoCompletoComparar, posARR):
    count = 0

    #if posARR == 0:
    #    print("entas?")
    
    #pos_repeated_clean = []
    iupiAr = []
    global pos_repeated_clean
    if posARR == 0:
        #print("testing")
        
        pos_repeated_clean = []
    else:
       
        pos_repeated_clean = pos_repeated_clean 
        #print("whats is the values:",  pos_repeated_clean )
       
    #clean_arr_data = []
    
    #print("####### verificarPosPalavras #######")
    #print(palavraDescoPos)
    #print("textoCompletoComparar")
    #print(textoCompletoComparar)

    for match in re.finditer(r'\b%s\b' % palavraDescoPos, textoCompletoComparar):
                clean_arr_data = []
                
                #print("match", count, match.group(), "start index", match.start(), "End index", match.end())
                pos_ini = int(match.start())
                
                pos_repeated_clean.append([pos_ini,match.group(),match.start(),match.end()])

                #Ordenar o array pela posicao inicial
                pos_repeated_clean.sort()

                #Evitar valores repetidos sobre a posicao das palavras
                unique_values = np.array(pos_repeated_clean)
                clean_arr_data = DataFrame(unique_values).drop_duplicates().values
                #print("pos_repeated_clean")
                #print(pos_repeated_clean)

                #print("clean_arr_data")
                #print(clean_arr_data)

    #print(clean_arr_data)
        
    return clean_arr_data


def verificarPosPalavrasCorretas(palavraDescoPos, textoCompletoComparar, posARR):
    count = 0

    #if posARR == 0:
    #    print("entas?")
    
    #pos_repeated_clean = []

    iupiAr_2 = []
    
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
    result_POS= []
    data = pd.DataFrame(None).to_json(orient='split',force_ascii=False)
    data2 = pd.DataFrame(None).to_json(orient='split',force_ascii=False)
 
    pos_repeated_clean = []
    clean_arr_data = []
    clean_arr_data_2 = []
    unique_values = []
 
   

    #print(json_ArrayFormat)
    removerTagHtml = remove(texto)
    #print(removerTagHtml)

    #limpar_formatacao_v2 = removerFormatacao(texto)
    #print(limpar_formatacao_v2)

    special_char_list = ["&nbsp;","$",'"',"@", "#", "&", "%",".",",","*","**","(",")","'",'"',"`","´",'<','>','{','}','=>','})','})}','}>',"<button type='button' class='btn_sinonimos' >","</button>", ]
    # using list comprehension
    op1 = "".join([k for k in removerTagHtml if k not in special_char_list])
    #print(f"op1 = ", op1)

    
    textoAcorrigir = op1
    arrayTexto = op1.split()
    arrayTexto_completo = op1.split()
    #O checker irá verificar os erros no texto que vem do front-end
    chkr.set_text(textoAcorrigir)

    palavrasSugeridas = {}
    arrayTotal_do_texto_escrito_set = []

    palavrasErradas = []
    palavras_a_corrigir = []


    p = re.compile("(?=\S*['-])([a-zA-Z'-]+)")
    
    #Rever a variável do hifen

    for err in chkr:
        # print("ERROR:", err.word)
        sug = err.suggest()
        trim = enchant.utils.trim_suggestions(err.word, sug, 3)

        print(trim)

        print(err.word)
        print(sug)
        palavraComHifen = [ s for s in sug if p.match(s) ]
    

        sug.remove(palavraComHifen[0])

        sug.insert(0,palavraComHifen[0])
        
        palavraMa = err.word

        #print("-------")
        #print(palavraMa)

        if (len(palavraMa) == 1):
            print(True)
        else:
            palavrasSugeridas.setdefault(err.word, []).append(sug)
            palavra_mal = "<span style='color:red;background-color: #ff000047;'>"+err.word+"</span>&nbsp;"
            #textoAcorrigir = textoAcorrigir.replace(err.word,palavra_mal)
            palavras_a_corrigir.append([err.word,palavra_mal])
            palavrasErradas.append(err.word)
          
            #palavrasErradas_POS = verificarPosPalavras(err.word, textoAcorrigir)
           
            #json_ArrayFormat.pop(1)

    print(palavrasSugeridas)
    


   
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
            #colocarPalavrasBemMal.append([colocarPalavrasBemMal[count]])
            arrayTexto.remove(count[0])
            print("------ numero----")
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


   

    for r in palavras_a_corrigir:
        # print(*r)
        # textoAcorrigir = textoAcorrigir.replace(*r)
        textoAcorrigir = textoAcorrigir.replace(*r)
 
    count=0

    pos_repeated_clean = []
    arr_format_html = []
    enviar_DadosFunc = []

    arrayTotal_do_texto_escrito_set = set(arrayTexto)
    palavrasErradas_v2 = set(palavrasErradas)

    matches = arrayTotal_do_texto_escrito_set.symmetric_difference(palavrasErradas_v2)
    array_matches_Found = list(matches)
    json_solve_array = list(matches)
    peso_coincidencia = len(json_solve_array)

    #print(matches)
    #print(arrayTotal_do_texto_escrito_set)

    #print("json_format")
    #print(json_ArrayFormat)
    #print(len(json_ArrayFormat))
    
    
            
    #print("Final ----- textoAcorrigir")
    #print(textoAcorrigir)
    

    

    #json_string = json.loads(json.dumps(textoAcorrigir)) 
    json_string_2 = json.loads(json.dumps(palavrasSugeridas)) 
    json_string_palavraMal = json.loads(json.dumps(palavrasErradas)) 
    links_Sinonimo = json.loads(json.dumps(json_solve_array)) 
    lista_palavrasBemMal = json.loads(json.dumps(colocarPalavrasBemMal))
    #lista_posPalavras = json.loads(json.dumps(palavras_POS))
    #print(envioInfo_pos_words)
    #result_POS = pd.DataFrame(palavras_POS).to_json(oriental_pos, orient='split')
    
    


    if len(palavras_POS) > 0:
        data =  pd.DataFrame(columns=palavras_POS).to_json(orient='split',force_ascii=False)
    else:
        #data =  pd.DataFrame(columns=["Nothing"]).to_json(orient='split',force_ascii=False)
        data = pd.DataFrame(columns=["nothing"]).to_json(orient='split',force_ascii=False)

    if len(palavras_POS_corretas) > 0:
        data2 =  pd.DataFrame(columns=palavras_POS_corretas).to_json(orient='split',force_ascii=False)
    else:
        data2 =  pd.DataFrame(columns=["nothing"]).to_json(orient='split',force_ascii=False)


   

    return json_string_2,json_string_palavraMal,links_Sinonimo,lista_palavrasBemMal,data,data2




#recebeTextoParaDetetar('<p>Olas")">Olas mundo")">**mundo** caza")">caza</p>')
#recebeTextoParaDetetar('Olás  <strong>do</strong> mundo jogar <strong>jogar</strong> jiz jogar <strong>jogar</strong>', "[[\"Olás\",0,\"regular\"],[\"do\",1,\"strong\"],[\"mundo\",2,\"regular\"],[\"jogar\",3,\"regular\"],[\"jogar\",4,\"strong\"],[\"jiz\",5,\"regular\"],[\"jogar\",6,\"regular\"],[\"jogar\",7,\"strong\"]]")
#recebeTextoParaDetetar('Olás  <strong>do</strong> mundo jogar <strong>jogar</strong> jiz jogar <strong>jogar</strong>', "[[\"Olás\",0,\"regular\"],[\"do\",1,\"strong\"],[\"mundo\",2,\"regular\"],[\"jogar\",3,\"regular\"],[\"jogar\",4,\"strong\"],[\"jiz\",5,\"regular\"],[\"jogar\",6,\"regular\"],[\"jogar\",7,\"strong\"]]")
#recebeTextoParaDetetar('guardachuva')
#recebeTextoParaDetetar('Olás  <strong>do</strong> mun do jogar <strong>jogar</strong> jiz jogar <strong>jogar</strong>', "[[\"Olás\",0,\"regular\"],[\"do\",1,\"strong\"],[\"mundo\",2,\"regular\"],[\"jogar\",3,\"regular\"],[\"jogar\",4,\"strong\"],[\"jiz\",5,\"regular\"],[\"jogar\",6,\"regular\"],[\"jogar\",7,\"strong\"]]")


