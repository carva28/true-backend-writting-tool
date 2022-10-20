import difflib as dl
    
# convert all character to lower case
def to_lowercase(item):
    output = item.lower()
    return output

# remove duplicates in list while maintaining order
def remove_duplicates(iList):
    output = list(dict.fromkeys(iList))
    return output
    
# remove all occurrences of item from list    
def remove_list_item(iList, item):
    output = list(filter(lambda a: a != item, iList))
    return output
    
# find closest items in list, default returns 3 matches
def find_closest_item(iList, item, lenght = 3):
    output = dl.get_close_matches(item, iList, lenght)
    return output
    
def is_upper_case(str):
    str = clean_special_chars(str)
    if str[0].isupper():
        return True
    return False

def starts_with_space(str):
    if str[0].isspace():
        return True
    return False

def ends_with_space(str):
    if str[-1].isspace():
        return True
    return False

def clean_special_chars(str):
    return ''.join(e for e in str if e.isalpha())