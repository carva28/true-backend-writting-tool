import difflib as dl

str1 = "Testes"
str2 = "testes"
str3 = "teste"
sug = ["exame","teste","test","teste","testes","téste"]

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

def remove_plural_words(iList, item = ""):
    output = [x for x in iList if check_plural_s(x, item)]
    
    print(output)
    return output
    
# Os substantivos e adjectivos que no singular terminam em a, e, i, o ou u formam o plural com o acrescentamento de um s     
def check_plural_s(item):
    output = item
    print(output)
    return output
    
remove_plural_words(sug)

