from evdev import UInput, ecodes as e

class Macro:
    
    def __init__(self, mK, kS, kSS):
        self.macroKey = mK
        self.keySequence = kS
        self.keyState = kSS

    def __str__(self):
        toReturn = "Macro Key: " + str(e.KEY[self.macroKey])
        toReturn += " Key Sequence:"
        for i in range(len(self.keySequence)):
            toReturn += " " + str(e.KEY[self.keySequence[i]])
            toReturn += ":" + str(self.keyState[i])

        return toReturn

    def macroKey(self):
        return self.macroKey

    def keySequence(self):
        return self.keySequence

    def execute(self):
        print "Executing " + e.KEY[self.macroKey] + " macro."
        ui = UInput()

        for i in range(len(self.keySequence)):
            ui.write(e.EV_KEY, self.keySequence[i], self.keyState[i]);
        ui.syn()
        ui.close()

    def saveProfile(self, profileName):
        f = open(profileName + ".mp", "w")
        f.write(str(self.macroKey) + "\n")
        for i in range(len(self.keySequence)):
            f.write(str(self.keySequence[i]) + ":" + str(self.keyState[i]) + "\n");
        f.close()

    @staticmethod
    def loadProfile(profileName):
        f = open(profileName + ".mp", "r")
        string = f.readline().rstrip("\n")
        macroKey = int(string)
        keySequence = []
        keyState = []
        string = f.readline().rstrip("\n")
        while string != "":
            index = string.index(":")
            keySequence.append(int(string[:index]))
            keyState.append(int(string[index + 1:]))
            string = f.readline().rstrip("\n")
        f.close()
        return Macro(macroKey, keySequence, keyState)

if __name__ == "__main__":
    testMacro = Macro(2, [3, 3, 4, 4, 5, 5, 6, 6], [1, 0, 1, 0, 1, 0, 1, 0])
    print testMacro
    testMacro.execute()
    testMacro.saveProfile("test")
    saveMacro = Macro.loadProfile("test")
    print saveMacro
    saveMacro.execute()
