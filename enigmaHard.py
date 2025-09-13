import random,sys,time,string

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

def print2(stringus,letterDelay=None):
    if letterDelay is not None:
        delay = letterDelay
    else:
        delay = 0.01
    for letter in stringus:
        sys.stdout.write(letter)
        time.sleep(delay)
    sys.stdout.flush()
    print()

def rotorgen(charset,offset,seed):  #takes string charset, returns string charset
    random.seed(seed)
    random.shuffle(charset)
    for carrier in range(offset):
        charset = advanceRotor(charset)

    return charset

def reflectorgen(charset,seed=None): #not mine (only thing ctrl c v)
    indices = list(range(len(charset)))
    if seed is not None:
        random.seed(seed)
    random.shuffle(indices)
    reflector = [None] * len(charset)
    for i in range(0, len(indices), 2):
        a, b = indices[i], indices[i+1]
        reflector[a] = b
        reflector[b] = a
    for carrier in range(len(reflector)):
        reflector[carrier] = str(reflector[carrier])
    return reflector

def basicReflector(charset): #is mine
    for carrier in range(0,len(charset),2):
        charset[carrier],charset[carrier+1] = charset[carrier+1],charset[carrier]
    return charset

def plugboardSettings(charset,swappingSeed,pairsSeed):
    allIndexes = list(range(len(charset)))#allindex = [x for x in range(len(allIndexes))]#print(allindex)
    if pairsSeed is not None:
        random.seed(pairsSeed)
    noPairs = random.randint(0,len(charset)//2)
    if swappingSeed is not None:
        random.seed(swappingSeed)
    for carrier in range(noPairs):
        currentCandidates = []

        for temp in range(2):
            randIndex = -99999999
            while randIndex not in allIndexes:
                randIndex = random.randint(0,(len(charset)//2) - 1)
            allIndexes.remove(randIndex)
            currentCandidates.append(randIndex)
        temp = charset[currentCandidates[0]]
        charset[currentCandidates[0]] = charset[currentCandidates[1]]
        charset[currentCandidates[1]] = temp
    return charset

def advanceRotor(list1):
    list2 = list1.copy()
    for carrier in range(len(list1) - 1, 0, -1):
        list1[carrier] = list1[carrier - 1]
    list1[0] = list2[len(list2) - 1]
    return list1

def letterToIndex(unmoddedCharset,letter):
    for index in range(len(unmoddedCharset)):
        if unmoddedCharset[index] == letter:
            return index
    return "NULL"

def process(letter,a,b,c,moveA,moveB,moveC,masonCharset):
    c0 = letterToIndex(masonCharset,letter)

    a = advanceRotor(a)
    moveA = (moveA + 1) % len(a)
    if notchA == moveA:
        b = advanceRotor(b)
        moveB = (moveB + 1) % len(b)
        if notchB == moveB:
            c = advanceRotor(c)
            moveC = (moveC + 1) % len(c)
            #don't bother checking c's notch (there is only 3 rotors for now)
    c1 = int(a[c0])
    c2 = int(b[c1])
    c3 = int(c[c2])
    c4 = int(r[c3])
    c5 = c.index(str(c4))
    c6 = b.index(str(c5))
    c7 = a.index(str(c6))
    return masonCharset[c7],a,b,c,moveA,moveB,moveC


#moveAin code
masonCharset = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                        '5', '6', '7', '8', '9', ' ', '.', ',', '-', '_', '\'', '!', '?', '"', '@', ';', ':', '(',
                        ')', '/', '#']  # no punctuation or uppercase for moveAsonCharset
mason = []
for carrier in range(len(masonCharset)):
    mason.append(str(carrier))

a = rotorgen(mason.copy(),3,1)  #standard rotor
b = rotorgen(mason.copy(),1,2)  #standard rotor
c = rotorgen(mason.copy(),1,3)  #standard rotor
#r = reflectorgen(mason.copy(),4)
r = basicReflector(mason.copy())

masonCharset = plugboardSettings(masonCharset.copy(),1,1)

if len(mason)%2 == 0:
    print2("VALID CHARSET DETECTED",0.01)
else:
    print2("INVALID CHARSET DETECTED, SYSTEM INSTABILITY WARNING",0.01)
notchA = 14
notchB = 2
notchC = 0

moveA = 0
moveB = 0
moveC = 0
letter = input(">>>")
for carrier in letter:
    carrier,a,b,c,moveA,moveB,moveC = process(carrier,a,b,c,moveA,moveB,moveC,masonCharset)
    sys.stdout.write(carrier)
    time.sleep(0.01)
print()
input("Press enter to exit")
