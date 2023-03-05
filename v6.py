import keyboard as kb
import threading as th
import time
import os

exceptionList = ['','esc','tab','space','z','f10','q','s','d','a','e','ctrl','alt','maj','windows gauche','enter','c','b','x','f9','f8']
key = ['']
status = ['off']
currentKey = [key[0]]

def spam(key,exceptionList,status,currentKey):
    while True:
        time.sleep(1)
        if currentKey[0] == key[0] and (currentKey[0] == 'f9' or currentKey[0] == 'f8'):
            continue
        if key[0] == 'f9' or key[0] == 'enter':
            status[0] = 'off'
            os.system('cls')
            print('F8: start\n'+'F9/ENTER: stop\n\nSTOPPED')
        elif key[0] == 'f8':
            status[0] = 'on'
            os.system('cls')
            print('F8: start\n'+'F9/ENTER: stop\n\nSTARTED')
        currentKey[0] = key[0]
        if status[0] == 'on':
            if key[0] not in exceptionList: 
                kb.press_and_release(key[0])
                

if __name__ == "__main__":
    x = th.Thread(target=spam, args=(key,exceptionList,status,currentKey))
    x.start()
    print('F8: start\n'+'F9/ENTER: stop\n\nSTOPPED')
    while True:
        key[0] = kb.read_key()
    
