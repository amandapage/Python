def firstVowel(phrase):
    wordlist = phrase.split()
    vowels = "aeiouAEIOU"
    for word in wordlist:
        for letter in word:
            if letter in vowels:
                idx = word.index(letter)
                break
    return idx
            
def checkPunct(word):
    for letter in word:
        if letter in "!?,.-:;":
            punctIdx = word.index(letter)
            punct = word[punctIdx]
            word = word.replace(punct,"")
            word += punct
    return word

def checkCap(word):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in word:
        if letter in ABC:
            word = word.lower()
            word = word[0].upper() + word[1:len(word)]
    return word

def igpay(phrase):
    wordlist = phrase.split()
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    newword = ""
    newphrase = ""

    for word in wordlist:
        if word[0] in consonants:
            idx = firstVowel(word)
            newword = word[idx:len(phrase)] + word[:idx] + "ay"
            newword = checkPunct(newword)
            newword = checkCap(newword)
            newphrase += newword + " "
        else:
            newword = word + "way"
            newword = checkPunct(newword)
            newword = checkCap(newword)
            newphrase += newword + " "
    newphrase = newphrase.rstrip()        
    return newphrase

