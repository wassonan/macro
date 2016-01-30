from evdev import UInput, ecodes as e

class Macro:
    
    def __init__(self, mK, kS, kSS):
        self.macroKey = mK
        self.keySequence = kS
        self.keyState = kSS
        print
        print len(self.keySequence)
        print len(self.keyState)

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

if __name__ == "__main__":
    testMacro = Macro(2, [3, 3, 4, 4, 5, 5, 6, 6], [1, 0, 1, 0, 1, 0, 1, 0])
    print testMacro
    testMacro.execute()
