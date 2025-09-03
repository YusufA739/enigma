import random,string

def listify(string):
    str_list = []
    for carrier in string:
        str_list.append(carrier)
    return str_list

def stringify(list):
    return delistify(list)

def delistify(list):
    list_str = ""
    for carrier in list:
        list_str += carrier
    return list_str

def rotorgen(charset,initcharset):  #takes string charset, returns string charset
    charset = listify(charset)
    random.shuffle(charset)
    charset1 = listify(charset)
    random.shuffle(charset1)
    return charset,charset1

def reflectorgen(charset):
    charset = listify(charset)
    random.shuffle(charset)
    middle = (len(charset))//2
    charset1 = charset[0:middle]
    charset = charset[middle:len(charset)-1]
    return charset,charset1

def advanceRotor(list1,list2):
    return advance(list1),advance(list2)

def advance(list1):
    list2 = list1.copy()
    for carrier in range(len(list1) - 1, 0, -1):
        list1[carrier] = list1[carrier - 1]
    list1[0] = list2[len(list2) - 1]
    return list1

def locateStatorIndex(list1,letter):
    for carrier in range(len(list1)):
        if letter == list1[carrier]:
            return carrier
    return -1

def getNextLetter(letter):

def process(letter,iA,iB,iC,nA,nB,nC,A1,A2,B1,B2,C1,C2,ref1,ref2,stator):
    iA += 1
    A1,A2 = advanceRotor(A1,A2)
    if nA == iA:
        iB += 1
        B1,B2 = advanceRotor(B1,B2)
        if nB == iB:
            iC += 1
            C1,C2 = advanceRotor(C1,C2)

    statorIndex = locateStatorIndex(stator,letter)
    if statorIndex == -1: return "NULL"
    else: pass




#main code
initCharset = string.ascii_lowercase + string.digits  #no punctuation or uppercase for now
numbers = []
for carrier in range(len(initCharset)):
    numbers.append(carrier)

staticRotor,discardThisValue = rotorgen(initCharset,initCharset)

a1,a2 = rotorgen(initCharset,initCharset)
b1,b2 = rotorgen(initCharset,a1)
c1,c2 = rotorgen(initCharset,b1)
r1,r2 = reflectorgen(c1)

indexA = 1
indexB = 1
indexC = 1

notchA = 2
notchB = 2
notchC = 0

while True:
    letter = input("enter letter: ")
    print(process(letter,indexA,indexB,indexC,notchA,notchB,notchC,a1,a2,b1,b2,c1,c2,r1,r2,staticRotor))