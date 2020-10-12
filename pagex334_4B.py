import string
def list2string(lst):
    gram = ""
    for i in range(len(lst)):
        gram += lst[i] + " "
    gram = gram.rstrip()
    return gram

def topngram(file,n):
    txtfile = open(file,'r')
    txt = txtfile.read().replace('\n', ' ') #makes one big string
    txt = txt.lower()
    abc = string.ascii_lowercase
    wordlst = []
    newlst=[]
    ignore = ["of","the","i","he","she","a","it","was","be","not","my","is"]
    ngrams = {}
    
    for char in txt:
        if char not in abc and char != " ":
            txt = txt.replace(char, "")

    wordlst = txt.split()
    for i in wordlst:
        if i in ignore:
            continue
        else:
            newlst.append(i)
                
    for i in range(len(newlst)):
        gram = newlst[i:i+n]
        if len(gram) < n:
            continue
        else:
            gram = list2string(gram)
            if gram not in ngrams:
                ngrams[gram] = 1
            else:
                ngrams[gram] += 1
    maxgram = max(ngrams, key = lambda elem: ngrams[elem])
    txtfile.close()
    return maxgram
        
        

