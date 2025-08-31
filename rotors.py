class Rotor:
    charset = ""
    charset1 = ""
    charset2 = ""
    start = 0
    notch = 10
    index = 0
    nextRotor = 0

    def __init__(self, start, notch, charset):
        self.start = start
        self.notch = notch
        self.charset = charset
    def type(self,letter):
        offset = 0
        for carrier in range(len(self.charset)):
            if self.charset[carrier] == letter:
                offset = carrier
        offset = offset - self.index

        self.index += 1
        if self.index == self.notch:
            self.incremnext(offset)
        if self.index >= len(self.charset):
            self.index -= len(self.charset)
        self.nextRotor.passivetype(offset)
    def incremnext(self,offset):
        self.index += 1
        offset = offset + 1
        if self.index == self.notch and type(self.nextRotor) != int:
            self.incremnext(offset)
        if self.index >= len(self.charset):
            self.index = 0
        if type(self.nextRotor) != int:
            return self.nextRotor.passivetype(offset)
        else:
            return self.passivetype(offset)
    def passivetype(self,index):

    def setNextRotor(self,rotor):
        self.nextRotor = rotor

    def getcharset(self):
        return self.charset
    def getnotch(self):
        return self.notch
    def getstart(self):
        return self.start
    def getIndex(self):
        return self.index