import enchant
from enchant.checker import SpellChecker

class CorrectionResult:
    def __init__(self, word="", correct=False, suggestion="", startRange=0, endRange=0):
        self.word = word
        self.correct = correct
        self.suggestion = suggestion
        self.startRange = startRange
        self.endRange = endRange

    def to_dict(self):
        return {"word": self.word, 
        "correct": self.correct, 
        "suggestion": self.suggestion, 
        "startRange": self.startRange,
        "endRange": self.endRange}

def checkText(text):
    chkr = SpellChecker(enchant.Dict("pt_PT"))
    words = [CorrectionResult()]
    i = 0
    lastIndex = len(text) - 1
    # text = text.replace("\n", "_")
    text = text.replace(u'\ufeff', '')

    for index, char in enumerate(text):
        
        if(char != " " and char != "\n"):
            words[i].word = words[i].word + char

        elif(len(words[i].word) > 0):
            words[i].correct = chkr.check(words[i].word)
            sugestion = chkr.suggest(words[i].word)
            words[i].suggestion = sugestion[0] if sugestion else ""
            words[i].endRange = index
            words[i].startRange = words[i].endRange - len(words[i].word)

            if(index != lastIndex):
                words.append(CorrectionResult())
                i += 1

    # delete empty last word
    if(words[-1].word == ""):
        del words[-1]
   
    results = [obj.to_dict() for obj in words]
    return results
