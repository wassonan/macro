#!/usr/bin/python
from macro import Macro
from evdev import InputDevice, list_devices, categorize, UInput, ecodes as e,\
    InputEvent, events

devices = [InputDevice(fn) for fn in list_devices()]

for i in range(len(devices)):
    print i, ": " , devices[i].name

choice = int(input())
chosenDevice = devices[choice]

print "You chose" + devices[choice].name
for device in devices:
    device.close()
chosenDevice = InputDevice(list_devices()[choice])

print "Please press program macro key"
programMacroKey = None

while programMacroKey == None:
    event = chosenDevice.read_one()
    if event != None:
        if event.type == e.EV_KEY and event.value == events.KeyEvent.key_down:
            programMacroKey = event.code

print e.KEY[programMacroKey]

recording = False
currentMacroKey = None;
currentMacro = []
currentState = []
macros = []


for event in chosenDevice.read_loop():
    if event.type == e.EV_KEY:

        # If the program macro key is hit
        if event.code == programMacroKey:
            if event.value == events.KeyEvent.key_down:
                if not recording:
                    print "Recording"
                    recording = True

                elif currentMacroKey == None or currentMacro == []:
                        print "Recording canceled"
                        recording = False
                        currentMacroKey = None
                        currentMacro = []
                        currentMacroState = []

                else:
                    newMacro = Macro(currentMacroKey, currentMacro, currentState)
                    print "Recording saved: " + str(newMacro)

                    macros.append(newMacro)
                    recording = False
                    currentMacroKey = None
                    currentMacro = []
                    currentState = []

        # If any other key is hit
        else:
            if recording:
                if currentMacroKey == None:
                    currentMacroKey = event.code

                else:
                    currentMacro.append(event.code)
                    currentState.append(event.value)

            else:
                for macro in macros:
                    if macro.macroKey == event.code:
                        macro.execute()
