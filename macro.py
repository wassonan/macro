from evdev import UInput, ecodes as e

class Macro:
    
    def __init__(self, mK, kS):
        self.macroKey = mK
        self.keySequence = kS

    def __str__(self):
        toReturn = "Macro Key: " + str(e.KEY[self.macroKey])
        toReturn += " Key Sequence:"
        for key in self.keySequence:
            toReturn += " " + str(e.KEY[key])

        return toReturn

    def macroKey(self):
        return self.macroKey

    def keySequence(self):
        return self.keySequence

    def execute(self):
        print "Executing " + e.KEY[self.macroKey] + " macro."
        ui = UInput()
        for key in self.keySequence:
            ui.write(e.EV_KEY, key, 1)
            ui.write(e.EV_KEY, key, 0)
        ui.syn()
        ui.close()

if __name__ == "__main__":
    testMacro = Macro(2, [3, 4, 5, 6, 7])
    print testMacro
    testMacro.execute()
