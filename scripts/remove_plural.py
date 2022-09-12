import difflib as dl

str1 = "Testes"
str2 = "testes"
str3 = "teste"
sug = ["exame","funis","alemães","perdigões","téste", "homens", "imanes"]

print("init: ")
print(sug)

# remove duplicates in list while maintaining order
def remove_duplicates(iList):
    output = list(dict.fromkeys(iList))
    print(output)
    return output
    
# remove all occurrences of item from list    
def remove_list_item(iList, item):
    output = list(filter(lambda a: a != item, iList))
    print(output)
    return output
    
# find closest items in list, default returns 3 matches
def find_closest_item(iList, item, lenght = 3):
    output = dl.get_close_matches(item, iList, lenght)
    print(output)
    return output
    
# convert all character to lower case
def to_lowercase(item):
    output = item.lower()
    print(output)
    return output

# 
def remove_plural_words(iList, item = ""):
    #output = [x for x in iList if check_plural_s(x, item)]
    
    output = [x for x in iList if check_plural_ls(x, item)]
    
    print(output)
    return output
    
# Os substantivos e adjectivos que no singular terminam em a, e, i, o ou u formam o plural com o acrescentamento de um s     
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

remove_plural_words(sug, "funil")

