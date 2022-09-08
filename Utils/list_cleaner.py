import difflib as dl

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