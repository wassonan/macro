from evdev import InputDevice, list_devices, categorize, ecodes, UInput, ecodes\
    as e, InputEvent
import time

devices = [InputDevice(fn) for fn in list_devices()]

for i in range(len(devices)):
    print i, ": " , devices[i].name

choice = int(input())
chosenDevice = devices[choice]

print "You chose" , devices[choice].name
#TODO Need to figure out a better way to prevent previous key presses
time.sleep(1)
print "Please press program macro key"
chosenDevice = InputDevice(list_devices()[choice])

#TODO read() seems to throw an IOError using read_loop() and break temporarily
for event in chosenDevice.read_loop():
    if event.type == e.EV_KEY:
        print(categorize(event))
        break;
