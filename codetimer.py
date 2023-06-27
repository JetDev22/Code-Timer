import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time
from beepy import beep


root = ttk.Window(title="simpleTimer", themename="darkly")


def runTimer():
    minutes = int(setTimer.get())
    total = int(setTimer.get())
    while minutes * 60 != 0:
        minutes = minutes - 1/60 
        timeRem.configure(amounttotal = total)
        timeRem.configure(amountused = round(minutes))
        time.sleep(1)
        root.update()
    beep(sound = 5)


# Timer Meter
timeRem = ttk.Meter(bootstyle="success", subtext="minutes remaining", subtextfont="-size 20 -weight bold", stripethickness=10, metersize=400, meterthickness=50, textfont="-size 50 -weight bold")
timeRem.pack(side=BOTTOM, padx=5, pady=10)

# Inputfield
setTimer = ttk.Entry(root, justify="center")
setTimer.pack(side=TOP, padx=40, pady=10)

# Butons
startButton = ttk.Button(root, text="Start", bootstyle=SECONDARY, command=lambda: runTimer())
startButton.pack(side=BOTTOM, padx=5, pady=10)

# Main App Loop
root.mainloop()