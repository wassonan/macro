from evdev import InputDevice, list_devices, categorize, UInput, ecodes as e,\
    InputEvent, events

devices = [InputDevice(fn) for fn in list_devices()]

for i in range(len(devices)):
    print i, ": " , devices[i].name

choice = int(input())
chosenDevice = devices[choice]

print "You chose" , devices[choice].name
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
            print(categorize(event))

print e.KEY[programMacroKey]

recording = False;
macros = []


for event in chosenDevice.read_loop():
    if event.type == e.EV_KEY and event.value == events.KeyEvent.key_down:
        if event.code == programMacroKey:
            

