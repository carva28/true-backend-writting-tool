# Remove palavras plural de uma palavra num lista 
def remove_plural_words(iList, item):
    output = [x for x in iList if check_plural_s(x, item)]
    if output != iList:
        return output

    output = [x for x in iList if check_plural_s_mn(x, item)]
    if output != iList:
        return output

    output = [x for x in iList if check_plural_es(x, item)]
    if output != iList:
        return output

    output = [x for x in iList if check_plural_oes(x, item)]
    if output != iList:
        return output
        
    output = [x for x in iList if check_plural_aes(x, item)]
    if output != iList:
        return output

    output = [x for x in iList if check_plural_is(x, item)]
    if output != iList:
        return output

    output = [x for x in iList if check_plural_ls(x, item)]
    if output != iList:
        return output

    return output
    
# plural com o acrescentamento de um s     
def check_plural_s(key, item):
    if item + "s" == key:
        return False
    return True
    
# Plural com o acrescentamento de um s, mas na escrita o m muda-se em n
# Ex.: homem - homens; armazém - armazéns; origem - origens
def check_plural_s_mn(key, item):
    if item[:-1] + "ns" == key:
        return False
    return True
    
# o plural com acrescentamento de –es: 
# Ex.: íman - ímanes; espécimen - especímenes; hífen - hífenes;
def check_plural_es(key, item):
    if item + "es" == key:
        return False
    return True
    
# o plural mudando o ão em ões: 
# Ex.: botão - botões; limão - limões; perdigão - perdigões;
def check_plural_oes(key, item):
    if item[:-2] + "ões" == key:
        return False
    return True
    
# o plural mudando o ão em ães: 
# Ex.: alemão - alemães; pão - pães; caimão - caimães;
def check_plural_aes(key, item):
    if item[:-2] + "ães" == key:
        return False
    return True
    
# plural mudando o l em –is:  
# Ex.: pardal - pardais; olival - olivais; gramatical - gramaticais;
def check_plural_is(key, item):
    if item[:-1] + "is" == key:
        return False
    return True    
    
#  plural mudando o –l em –s: 
#  funil - funis; peitoril -peitoris; ovil - ovis;
def check_plural_ls(key, item):
    if item[:-1] + "s" == key:
        return False
    return True    
