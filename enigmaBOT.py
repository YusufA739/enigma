import random,sys,time,string,discord
from discord import Client, Intents



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

def process(letter,a,b,c,moveA,moveB,moveC,msc):
    c0 = letterToIndex(msc,letter)

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

#bot code
file1 = open("token.txt","r")
data = file1.readline()
file1.close()

client = discord.Client(intents=discord.Intents.all())
run_once = True

masonCharset = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                        '5', '6', '7', '8', '9', ' ', '.', ',', '-', '_', '\'', '!', '?', '"', '@', ';', ':', '(',
                        ')']  # no punctuation or uppercase for moveAsonCharset
masonCharset = plugboardSettings(masonCharset.copy(), 1, 1)
a,b,c,r,mason = None,None,None,None,None

notchA = 0
notchB = 0
notchC = 0

moveA = 0
moveB = 0
moveC = 0

@client.event
async def on_message(message):
    global run_once,masonCharset,notchA,notchB,notchC,moveA,moveB,moveC,a,b,c,r,mason

    if message.author != client.user:
        masonCharset = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                        '5', '6', '7', '8', '9', ' ', '.', ',', '-', '_', '\'', '!', '?', '"', '@', ';', ':', '(',
                        ')', '/', '#']  # no punctuation or uppercase for moveAsonCharset
        mason = []
        for carrier in range(len(masonCharset)):
            mason.append(str(carrier))

        a = rotorgen(mason.copy(), 3, 1)  # standard rotor
        b = rotorgen(mason.copy(), 1, 2)  # standard rotor
        c = rotorgen(mason.copy(), 1, 3)  # standard rotor
        # r = reflectorgen(mason.copy(),4)
        r = basicReflector(mason.copy())

        masonCharset = plugboardSettings(masonCharset.copy(), 1, 1)

        notchA = 4
        notchB = 6
        notchC = 0

        moveA = 0
        moveB = 0
        moveC = 0

        messageWords = message.content.lower().strip().split() #default split() is by spaces (" ") and strip is to remove whitespace from start and end (defualt)
        if messageWords[0] == "/help" or messageWords[0] == "!help" or messageWords[0] == "/encodehelp" or messageWords[0] == "!encodehelp":
            await message.channel.send("Type /start then /encode to initalise then send a message respectively (RESET BEFORE TYPING NEW REPORTS/MESSAGES)")
        elif messageWords[0] == "!encode" or messageWords[0] == "/encode": #allow for there to be a use of the old command format (!) and the new command format (/) but make
            #sure that the command is at the start (don't use contains or in because I want it to be at the beginning to match other bots)
            messageContent = message.content.strip() #strips the leading and trailing whitespace by default
            if messageContent == "":
                await message.channel.send("PUT SOME WORDS WITH THE COMMAND THEN!!!")
            else:
                messageContent = message.content[8:]
                string = ""

                for carrier in messageContent:
                    carrier,a,b,c,moveA,moveB,moveC = process(carrier,a,b,c,moveA,moveB,moveC,masonCharset)
                    string += carrier
                await message.channel.send(string)
        #else:
            #await message.channel.send("RUN /start or /help")

client.run(data)