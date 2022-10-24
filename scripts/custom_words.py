import enchant

file_path = "data\pwl.txt"
pwl = enchant.request_pwl_dict(file_path)

def add_personal_word(word):
    if(pwl.check(word) == False):
        return pwl.add(word)

def remove_personal_word(word):
    pwl.remove(word)

def get_all_words():
    words = []

    with open(file_path, 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
            print(x)

            words.append(x)
    
    return words
