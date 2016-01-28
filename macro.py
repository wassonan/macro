from evdev import UInput, ecodes as e

class Macro:
    
    def __init__(self, mK, kS):
        self.macroKey = mK
        self.keySequence = kS

    def __str__(self):
        toReturn = "Macro Key: ", e.KEY[self.macroKey]

    def macroKey(self):
        return self.macroKey

    def keySequence(self):
        return self.keySequence

