import random,string,sys

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
    random.shuffle(charset)
    for carrier in range(offset):
        charset = advanceRotor(charset)

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

def process(letter,mA,mB,mC,nA,nB,nC,A,B,C,ref1,ref2,statorLetters):
    c0 = letterToIndex(statorLetters,letter)

    A = advanceRotor(A)
    mA += 1
    if mA >= len(A):
        mA = 0
    if mB >= len(B):
        mB = 0
    if mC >= len(C):
        mC = 0
    
    if nA == mA:
        B = advanceRotor(B)
        mB += 1
        if nB == mB:
            C = advanceRotor(C)
            mC += 1
            #don't bother checking C's notch (there is only 3 rotors for now)
    c1 = int(A[c0])
    c2 = int(B[c1])
    c3 = int(C[c2])

    if c3 >= len(ref1):
        c3 -= len(ref1)
        cRef1 = int(ref2[c3])#check value in reflector 2 to go to that value in reflector 1
        cDiskPreIndex = ref1[cRef1]#check value only so we can locate index so we can map reflector 1 back to rotor C index
        c4 = letterToIndex(ref1,cDiskPreIndex)#map reflector 1 value back to rotor C index
    else:
        cRef2 = int(ref1[c3])
        cDiskPreIndex = ref2[cRef2]
        c4 = letterToIndex(ref2,cDiskPreIndex)
        c4 = c4 + len(ref1)

    c5 = int(C[c4])
    c6 = int(B[c5])
    c7 = int(A[c6])

    return c7,mA,mB,mC,A,B,C


#main code
masonCharset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  #no punctuation or uppercase for masonCharset
mason = []  #the numbers, mason!!!!!!! what do they mean?????
halfMason = []
for carrier in range(len(masonCharset)):
    mason.append(str(carrier))
for carrier in range(int(len(masonCharset)/2)):
    halfMason.append(str(carrier))

#masonScramble = mason.copy()  #copy index order
#random.shuffle(masonScramble)  #scramble index order

a = rotorgen(mason.copy(),1)  #standard rotor
b = rotorgen(mason.copy(),1)  #standard rotor
c = rotorgen(mason.copy(),1)  #standard rotor
#refToRotor = rotorgen(mason.copy(),1)  #points from reflector index back to rotor index (allows for conversion to reflector index and back to rotor index) (can be replaced by using mirror pair reflector with full indexes spread accross both lists r1 and r2)
r1,r2 = rotorgen(halfMason.copy(),1),rotorgen(halfMason.copy(),1)  #points to reflector indexes only

print(len(mason),"OPERATOR, CHECK THIS IS EVEN. ADD CHARACTERS TO CHARSET IF NOT EVEN")
for carrier in range(len(a)):
    sys.stdout.write(a[carrier] + " ")
print()
for carrier in range(len(b)):
    sys.stdout.write(b[carrier] + " ")
print()
for carrier in range(len(c)):
    sys.stdout.write(c[carrier] + " ")
print()
for carrier in range(len(r1)):
    sys.stdout.write(r1[carrier] + " ")
print()
for carrier in range(len(r2)):
    sys.stdout.write(r2[carrier] + " ")
print()



inpA = input("enter A rotor or press enter for new rotors:")
if inpA == "":
    a = "5 17 28 27 18 14 29 19 4 8 9 20 31 1 21 3 15 0 22 34 7 12 13 16 11 35 30 26 6 23 32 25 33 24 2 10"
    b = "16 10 17 31 3 12 4 27 22 8 26 30 19 15 0 24 33 11 34 2 6 21 18 9 32 14 7 28 35 1 25 20 29 23 5 13"
    c = "35 20 15 33 30 5 8 34 27 25 24 6 28 0 16 17 29 14 23 12 4 22 9 19 10 26 32 18 11 3 2 31 1 7 21 13"
    r1 = "15 17 5 7 12 3 0 8 6 9 1 11 2 10 13 14 16 4"
    r2 = "4 0 5 2 15 3 1 16 17 13 10 14 11 7 12 8 9 6"
    a = a.split(" ")
    b = b.split(" ")
    c = c.split(" ")
    r1 = r1.split(" ")
    r2 = r2.split(" ")
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

notchA = 10
notchB = 10
notchC = 0

moveA = 0
moveB = 0
moveC = 0



while True:
    letter = input("enter letter: ")
    finalIndex,moveA,moveB,moveC,a,b,c = process(letter,moveA,moveB,moveC,notchA,notchB,notchC,a,b,c,r1,r2,masonCharset)
    print(masonCharset[finalIndex])
