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

def check_last_char(word):
    valid_chars = ["?", "!", ",", ";", "'", '"', ":"]

    # check if is valid special char
    if any(word[-1] in char for char in valid_chars):
        if word[0] == "'" or word[0] == '"':
            return word[1:-1]
        elif word[-1] == "." and word[-2] == '"':
            return word[:-2]
        elif word[-1] == "." and word[-2] == "'":
            return word[:-2]     
        else:
            return word[:-1]
    else:
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
        # if last char is valid special char        
        word.word = check_last_char(word.word)

        word.correct = chkr.check(word.word)
        sugestion = chkr.suggest(word.word)
        word.suggestion = sugestion[0] if sugestion else ""
   
    results = [obj.to_dict() for obj in words]
    return results
