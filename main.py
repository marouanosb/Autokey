import tkinter as tk
import tkinter.font as tkFont
import keyboard as kb
from threading import Thread, Event

stopThread = Event()    #if keyboardThread is running(clear) or not(set)
stopThread.set()  

class App:
    def __init__(self, root):
        #setting title
        root.title("Autokey")
        #setting window size
        width=400
        height=150
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background='#424549')

        startStopButton=tk.Button(root)
        startStopButton["bg"] = "#1e2124"
        ft = tkFont.Font(family='Times',size=10)
        startStopButton["font"] = ft
        startStopButton["fg"] = "#7289da"
        startStopButton["justify"] = "center"
        startStopButton["text"] = "Start/Stop"
        startStopButton.place(x=110,y=20,width=90,height=25)
        startStopButton["command"] = self.startStopButton_command

        startStopContainer=tk.Entry(root)
        ft = tkFont.Font(family='Times',size=10)
        startStopContainer["font"] = ft
        startStopContainer["fg"] = "#333333"
        startStopContainer["justify"] = "center"
        startStopContainer.place(x=220,y=20,width=70,height=25)
        startStopContainer.insert(0,'f9')

        twoPoints=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        twoPoints["font"] = ft
        twoPoints["bg"] = '#424549'
        twoPoints["fg"] = "#ffffff"
        twoPoints["justify"] = "center"
        twoPoints["text"] = ":"
        twoPoints.place(x=200,y=20,width=20,height=25)

        safeListContainer=tk.Entry(root)
        ft = tkFont.Font(family='Times',size=10)
        safeListContainer["font"] = ft
        safeListContainer["fg"] = "#333333"
        safeListContainer["justify"] = "center"
        safeListContainer["text"] = "safeListContainer"
        safeListContainer.place(x=20,y=70,width=360,height=25)

        editButton=tk.Button(root)
        editButton["bg"] = "#1e2124"
        ft = tkFont.Font(family='Times',size=10)
        editButton["font"] = ft
        editButton["fg"] = "#7289da"
        editButton["justify"] = "center"
        editButton["text"] = "Edit"
        editButton.place(x=120,y=110,width=70,height=25)
        editButton["command"] = self.editButton_command

        doneButton=tk.Button(root)
        doneButton["bg"] = "#1e2124"
        ft = tkFont.Font(family='Times',size=10)
        doneButton["font"] = ft
        doneButton["fg"] = "#7289da"
        doneButton["justify"] = "center"
        doneButton["text"] = "Done"
        doneButton.place(x=210,y=110,width=70,height=25)
        doneButton["command"] = self.doneButton_command


    def startStopButton_command(self):
            if stopThread.is_set() :
                stopThread.clear()
            else : stopThread.set()
                

    def editButton_command(self):
        print("command")


    def doneButton_command(self):
        print("command")


def keyLogging(stopThread):
    kb.wait('f9')
    while True:
        event = kb.read_event()
        if event.event_type == kb.KEY_UP:
            key = event.name
            if key == 'f9' and stopThread.is_set():
                break
            print(key +' pressed')
    return

def keyRepeat(key):
    kb.send(key)
    return


if __name__ == "__main__":
    keyboardThread = Thread(target=keyLogging, args=(stopThread,))
    keyboardThread.start()

    root = tk.Tk()
    app = App(root)
    root.mainloop()

    keyboardThread.join()

    
    
