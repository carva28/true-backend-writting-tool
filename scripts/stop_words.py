from nltk.tokenize import word_tokenize

file_path = "./data/black_list.txt"

simple_text = "A professora é uma puta de merda."

def filter_list(iList):
    tokenized_list = word_tokenize(iList)
    stop_words = get_stop_words()

    filtered_list = [x for x in tokenized_list if x not in stop_words]

    return filtered_list

def get_stop_words():
    words = []

    with open(file_path, 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            words.append(x)
    
    return words

def add_stop_words(word_list):
    tokenized_list = word_tokenize(word_list)

    with open(file_path, 'a') as fp:
        for item in tokenized_list:
            # check if item already exists
            if check_if_exists(item) == False:
                # write each item in lower case on a new line
                fp.write("%s\n" % item.lower())

    return("Added words to black list")

def remove_stop_word(word):
    with open(file_path, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i.strip('\n') != word:
                f.write(i)
        f.truncate()

    return("Removed word from black list")

def check_if_exists(word):
    words = get_stop_words()

    if word.lower() in words:
        return True
    return False

#add_stop_words("ConA pUta mERda")
#filter_list(simple_text)
#remove_stop_word("ca")