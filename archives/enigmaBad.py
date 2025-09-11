import random,string

from rotors import Rotor


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

def rotorgen(charset):  #takes string charset, returns string charset
    charset = listify(charset)
    random.shuffle(charset)
    charset1 = listify(charset)
    random.shuffle(charset1)
    return stringify(charset),stringify(charset1)

def reflectorgen(charset):
    charset = listify(charset)
    random.shuffle(charset)
    middle = (len(charset))//2
    charset1 = charset[0:middle]
    charset = charset[middle:len(charset)-1]
    return stringify(charset),stringify(charset1)


#main code
initCharset = string.ascii_letters + string.digits  #no punctuation for now, even letters needed

a,b = rotorgen(initCharset)
c,d = rotorgen(a)
e,f = rotorgen(b)
g,h = reflectorgen(c)

rotor1 = Rotor(0,1,a)
rotor2 = Rotor(0,4,b)
rotor3 = Rotor(0,1,c)
rotor4 = Rotor(0,1,g)
rotor1.setNextRotor(rotor2)
rotor2.setNextRotor(rotor3)
rotor3.setNextRotor(rotor4)
print(rotor1.getcharset())
print(rotor2.getcharset())
print(rotor3.getcharset())
print(rotor4.getcharset())

