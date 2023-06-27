import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
from beepy import beep


root = ttk.Window(title="simpleTimer", themename="darkly")

# Global variable
global stopped
stopped = False

def runTimer():
    global stopped
    stopped = False
    minutes = int(setTimer.get())
    total = int(setTimer.get())
    while minutes > 0:
        minutes = minutes - 1/60 
        timeRem.configure(amounttotal = total)
        timeRem.configure(amountused = round(minutes))
        root.after(1000, root.update())
        if stopped == True:
            timeRem.configure(amountused = 0)
            setTimer.delete(0,END)
            break
    beep(sound = 5)

def stopTimer():
    global stopped
    stopped = True
    return stopped

# Timer Meter
timeRem = ttk.Meter(bootstyle="success", subtext="minutes remaining", subtextfont="-size 20 -weight bold", stripethickness=10, metersize=400, meterthickness=50, textfont="-size 50 -weight bold")
timeRem.pack(side=BOTTOM, padx=5, pady=10)

# Inputfield
setTimer = ttk.Entry(root, justify="center")
setTimer.pack(side=TOP, padx=40, pady=10)

# Butons
startButton = ttk.Button(root, text="Start", bootstyle=SUCCESS, command=lambda: runTimer())
startButton.pack(expand=True, pady=10)

test = ttk.Button(root, text="Stop", bootstyle=DANGER, command=lambda: stopTimer())
test.pack(expand=True, pady=10)

# Main App Loop
root.mainloop()