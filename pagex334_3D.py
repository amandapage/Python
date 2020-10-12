def stockStat(csv,yr):
    stockfile = open(csv,"r")
    stockfile.readline()
    mylist = []
    yr = str(yr)
    
    for line in stockfile:
        values = line.split(",")
        date = values[0]
        if values[4] == "null":
            values[4] = values[4].replace("null","0")
        close = float(values[4])
        stockyrdate = date[:4]
        if stockyrdate == yr:
            mylist.append(close)
    avg = sum(mylist)/len(mylist)
    company = csv.replace(csv[-4:],"")
    stockfile.close()
    return("The average closing value of "+company+" in "+yr+" was $"+"{:.2f}".format(avg)+".")

def convertDate(date):
    yr = date[:4]
    numMonth = date[5:7]
    month = ""
    if date[8] == '0':
        day = date[-1]
    else:
        day = date[-2:]
    if numMonth == '01':
        month = "January"
    elif numMonth == '02':
        month = "February"
    elif numMonth == '03':
        month = "March"
    elif numMonth == '04':
        month = "April"
    elif numMonth == '05':
        month = "May"
    elif numMonth == '06':
        month = "June"
    elif numMonth == '07':
        month = "July"
    elif numMonth == '08':
        month = "August"
    elif numMonth == '09':
        month = "September"
    elif numMonth == '10':
        month = "October"
    elif numMonth == '11':
        month = "November"
    else:
        month = "December"
    return (month + " " +day+", "+yr)
        
def maxGain(csv):
    stockfile = open(csv,"r")
    stockfile.readline()
    prices = []
    dates = []
    for line in stockfile:
        values = line.split(",")
        if values[0] == "null" or values[1] == "null" or values[2] == "null" or values[4] == "null":
            values[0] = values[0].replace("null","0")
            values[1] = values[1].replace("null","0")
            values[2] = values[2].replace("null","0")
            values[4] = values[4].replace("null","0")
        close = float(values[4])
        openn = float(values[1])
        price = close - openn
        prices.append(price)
        dates.append(values[0])
    maxgain = max(prices)
    gainIndx = prices.index(maxgain)
    numdate = dates[gainIndx]
    date = convertDate(numdate)
    company = csv.replace(csv[-4:],"")
    stockfile.close()
    return ("The largest single day gain for "+company+" was "+date+".")
