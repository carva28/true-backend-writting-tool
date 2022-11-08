import enchant
from enchant.checker import SpellChecker

chkr = SpellChecker(enchant.DictWithPWL("pt_PT", "data\personal_word_list.txt"))

class CorrectionResult:
    def __init__(self, word="", correct=False, suggestion="", start_range=0, end_range=0):
        self.word = word
        self.correct = correct
        self.suggestion = suggestion
        self.startRange = start_range
        self.endRange = end_range

    def to_dict(self):
        return {"word": self.word, 
        "correct": self.correct, 
        "suggestion": self.suggestion, 
        "startRange": self.startRange,
        "endRange": self.endRange}

def check_special_char(word):
    new_word = word
    valid_second_last_chars = [ ";", ".", "]", "'", '"', ")", "?", "!" ]
    valid_last_chars = [ ",", ";", ".", "]", "'", '"', ")", ":","?", "!" ]
    valid_first_chars = [ "'", '"', "(" ,"["]
    valid_second_chars = [ "'", '"', "(" ,"["]

    # check if last char is valid stop char
    if any(new_word[-1] in char for char in valid_last_chars):
        new_word = new_word[:-1]

        # check if second last char is also valid
        if any(new_word[-1] in char for char in valid_second_last_chars):
            # check if last and second last chars are different
            if(word[-1] != word[-2]):
                new_word = new_word[:-1]

    # check if first char is valid
    if any(new_word[0] in char for char in valid_first_chars):
        new_word = new_word[1:]

        # check if second char is also valid
        if any(new_word[0] in char for char in valid_second_chars):
            # check if first and second chars are different
            if(word[0] != word[1]):
                new_word = new_word[1:]

    return new_word


def check_valid_number(word):
    valid_chars = ["%", "$", "£", "€", "º", "ª", ",", ".", "!", "?", ":"]

    # last char is valid
    if any(word[-1] in char for char in valid_chars):
        word = word[:-1]

    return word    

def check_text(text):
    words = [CorrectionResult()]
    i = 0
    lastIndex = len(text) - 1
    text = text.replace(u'\ufeff', '')

    for index, char in enumerate(text):
        
        if char != " " and char != "\n":
            words[i].word = words[i].word + char

        elif len(words[i].word) > 0:
            words[i].endRange = index
            words[i].startRange = words[i].endRange - len(words[i].word)

            if index != lastIndex:
                words.append(CorrectionResult())
                i += 1

    # delete empty last word
    if words[-1].word == "":
        del words[-1]

    for word in words:
        print("initial word ", word.word)
        # check if is number with special char
        if(word.word[0].isnumeric()):
            word.word = check_valid_number(word.word)
        else:
            # check if last char is valid        
            word.word = check_special_char(word.word)

        word.correct = chkr.check(word.word)
        sugestion = chkr.suggest(word.word)
        word.suggestion = sugestion[0] if sugestion else ""

        print(word.word, " ", word.correct)
        print("-----")

   
    results = [obj.to_dict() for obj in words]

    return results
