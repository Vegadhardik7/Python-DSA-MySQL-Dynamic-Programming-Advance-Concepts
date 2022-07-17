'''
Input: hello     Output: ehllo
Input:eLEPhAnt   Output: AEehLnPt
'''

def sortingAplhaVaue(data):
    sortvalues = sorted(list(data))
    lowerlst = sorted(list(data.lower()))
    caplst = []
    newdata = ''

    for i in sortvalues:
        if i.isupper():
            caplst.append(i)

    for x in lowerlst:
        if caplst.count(x.upper()) != 0:
            newdata += x.upper()
            caplst.pop(caplst.index(x.upper()))
        else:
            newdata += x

    return newdata

data = sortingAplhaVaue("eLEPhAnt")
print(data)
