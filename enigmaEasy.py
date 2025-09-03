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

def rotorgen(charset,offset):  #takes string charset, returns string charset
    charset = listify(charset)
    random.shuffle(charset)
    for carrier in range(offset):
        charset = advanceRotor(charset)

    return charset

def reflectorgen(charset,offset):
    charset = listify(charset)
    random.shuffle(charset)
    for carrier in range(offset):
        charset = advanceRotor(charset)

    middle = (len(charset))//2

    charset1 = charset[0:middle] #change this from charset1 to charset and use the prints to see why I did it like this
    charset = charset[middle-1:len(charset)-1]
    #print(len(charset))
    #print(len(charset1))
    return charset,charset1

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

def process(letter,mA,mB,mC,nA,nB,nC,A,B,C,ref1,ref2,statorLetters):
    c0 = letterToIndex(statorLetters,letter)

    A = advanceRotor(A)
    mA += 1
    if nA == mA:
        B = advanceRotor(B)
        mA = 0
        mB += 1
        if nB == mB:
            C = advanceRotor(C)
            mB = 0
            mC += 1
            #don't bother checking C's notch (there is only 3 rotors for now)
    c1 = int(A[c0])
    c2 = int(B[c1])
    c3 = int(C[c2])

    if c3 >= len(ref1):
        c3 -= len(ref1)
        c4 = int(ref2[c3])
    else:
        c4 = int(ref1[c3])

    c5 = int(C[c4])
    c6 = int(B[c5])
    c7 = int(A[c6])

    return c7,mA,mB,mC


#main code
masonCharset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  #no punctuation or uppercase for masonCharset
mason = []  #the numbers, mason!!!!!!! what do they mean?????
for carrier in range(len(masonCharset)):
    mason.append(str(carrier))

#masonScramble = mason.copy()  #copy index order
#random.shuffle(masonScramble)  #scramble index order

a = rotorgen(mason,1)  #
b = rotorgen(mason,1)  #
c = rotorgen(mason,1)  #
r1,r2 = reflectorgen(mason,1)  #

print(len(mason),"OPERATOR, CHECK THIS IS EVEN. ADD CHARACTERS TO CHARSET IF NOT EVEN")
string = ""
for carrier in a:
    string += carrier + " "
print(string)
string = ""
for carrier in b:
    string += carrier + " "
print(string)
string = ""
for carrier in c:
    string += carrier + " "
print(string)
string = ""
for carrier in r1:
    string += carrier + " "
print(string)
string = ""
for carrier in r2:
    string += carrier + " "
print(string)


inpA = input("enter A rotor or press enter for new rotors:")
if inpA == "":
    pass
else:
    inpB = input("enter B rotor:")
    inpC = input("enter C rotor:")
    inpR1 = input("enter Reflector Half 1:")
    inpR2 = input("enter Reflector Half 2:")
    inpA = inpA.split(" ")
    inpB = inpB.split(" ")
    inpC = inpC.split(" ")
    inpR1 = inpR1.split(" ")
    inpR2 = inpR2.split(" ")
    a = inpA
    b = inpB
    c = inpC
    r1 = inpR1
    r2 = inpR2

notchA = 2
notchB = 2
notchC = 1

moveA = 0
moveB = 0
moveC = 0



while True:
    letter = input("enter letter: ")
    finalIndex,moveA,moveB,moveC = process(letter,moveA,moveB,moveC,notchA,notchB,notchC,a,b,c,r1,r2,masonCharset)
    print(masonCharset[finalIndex])
