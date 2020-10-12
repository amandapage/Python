def markup2HTML(file):
    origFile = open(file, 'r')
    newFileName = file[:-3] + "html"
    newFile = open(newFileName, 'w')
    txt = origFile.read().replace('\n', '<br/>')
    newFile.write("<html><head> <title> CSCI1133 Markup </title> </head><body>")
    newTxt = ""
    countStar = 0
    countDash = 0
    countSlash = 0
    countLine = 0
    countHash = 0
    i = 0
    while i < len(txt):
        #bold
        if txt[i] == "*" and countStar%2 == 0: 
            newTxt +="<b>" 
            countStar += 1
        elif txt[i] == "*" and countStar%2 != 0:
            newTxt += "</b>"
            countStar += 1
        #underline
        elif txt[i] == "_" and countDash%2 == 0:
            newTxt += "<u>"
            countDash += 1
        elif txt[i] == "_" and countDash%2 != 0:
            newTxt += "</u>"
            countDash += 1
        #italicize
        elif txt[i] == "/" and countSlash%2 == 0 and txt[i+1] != ">":
            newTxt += "<i>"
            countSlash += 1
        elif txt[i] == "/" and countSlash%2 != 0  and txt[i+1] != ">":
            newTxt += "</i>"
            countSlash += 1
        #strikethrough
        elif txt[i] == "-" and txt[i+1] == "-" and countLine%2 == 0:
            newTxt += "<strike>"
            countLine += 1
            i+=1
        elif txt[i] == "-" and txt[i+1] == "-" and countLine%2 != 0:
            newTxt += "</strike>"
            countLine += 1
            i+= 1
        #color
        elif txt[i] == "#" and countHash%2 == 0:
            newTxt += "<span style='color:#" + txt[i+1:i+7] + "'>"
            countHash += 1
            i+=6
        elif txt[i] == "#" and countHash%2 != 0:
            newTxt += "</span>"
            countHash += 1
        else:
            newTxt += txt[i]
        #increase index
        i += 1

    newFile.write(newTxt)       
    newFile.write("</body></html>")
    newFile.close()





   
