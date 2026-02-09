#attention ce ne sont pas des lettres classiques mais des emojis unicode et ça m'a pris très (trop) longtemps à faire
letters = ["🇦", "🇨", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿"]
def react(word):
    if hasNoRepeats(word):
        reactReturn = []
        for i in word.lower():
            reactReturn.append(letters[ord(i.lower())-97])
        return reactReturn
    else:
        return []

def hasNoRepeats(string):
    return len(set(string)) == len(string)