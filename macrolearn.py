from evdev import InputDevice, list_devices, categorize, ecodes, UInput, ecodes\
    as e

devices = [InputDevice(fn) for fn in list_devices()]
print list_devices()

for dev in devices:
    print(dev.fn, dev.name, dev.phys)

dev = InputDevice("/dev/input/event2")
print dev

ui = UInput()
ui.write(e.EV_KEY, e.KEY_H, 1)
ui.write(e.EV_KEY, e.KEY_H, 0)
ui.write(e.EV_KEY, e.KEY_E, 1)
ui.write(e.EV_KEY, e.KEY_E, 0)
ui.write(e.EV_KEY, e.KEY_L, 1)
ui.write(e.EV_KEY, e.KEY_L, 0)
ui.write(e.EV_KEY, e.KEY_L, 1)
ui.write(e.EV_KEY, e.KEY_L, 0)
ui.write(e.EV_KEY, e.KEY_O, 1)
ui.write(e.EV_KEY, e.KEY_O, 0)
ui.write(e.EV_KEY, e.KEY_SPACE, 1)
ui.write(e.EV_KEY, e.KEY_SPACE, 0)
ui.write(e.EV_KEY, e.KEY_W, 1)
ui.write(e.EV_KEY, e.KEY_W, 0)
ui.write(e.EV_KEY, e.KEY_O, 1)
ui.write(e.EV_KEY, e.KEY_O, 0)
ui.write(e.EV_KEY, e.KEY_R, 1)
ui.write(e.EV_KEY, e.KEY_R, 0)
ui.write(e.EV_KEY, e.KEY_L, 1)
ui.write(e.EV_KEY, e.KEY_L, 0)
ui.write(e.EV_KEY, e.KEY_D, 1)
ui.write(e.EV_KEY, e.KEY_D, 0)
ui.write(e.EV_KEY, e.KEY_RIGHTSHIFT, 1)
ui.write(e.EV_KEY, e.KEY_1, 1)
ui.write(e.EV_KEY, e.KEY_RIGHTSHIFT, 0)
ui.write(e.EV_KEY, e.KEY_1, 0)
ui.write(e.EV_KEY, e.KEY_ENTER, 1)
ui.write(e.EV_KEY, e.KEY_ENTER, 0)
ui.syn()
ui.close()

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
