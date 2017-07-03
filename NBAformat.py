def removeDuplicates(redundantList):
    uniqueList = []
    prev = None
    for e in redundantList:
        if e != prev:
            uniqueList.append(e)
            prev = e

    return uniqueList

def makePairList(myList, delimiter):
    pairList = []
    for e in myList:
        pair = e.split(delimiter)
        pairList.append(pair)

    return pairList

def format(rawList):
    uniqueList = removeDuplicates(rawList)
    pairList = makePairList(uniqueList,"-")
    intPairList = [map(int,x) for x in pairList]

    return intPairList
