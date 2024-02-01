import secrets
import tkinter as tk

low = 1
high = 21
XanPlayers = ["Киос", "Хильда", "Тел", "Неудача", "Кори"]
XanInit = [3, 2, 3, 4, -1]
iterator = 0  # Added iterator variable to track the XanInit list

def RandomForPlayers():
    players = int(CountOfPlayers.get())
    z = 0
    for i in range(players):
        z = z + 38
        randomOut = secrets.randbelow(high - low) + low
        print(randomOut)
        RandomOfPlayers = tk.Label(window, text=int(randomOut) + int(XanIn()), font=("Arial Bold", 12), fg="lime", bg="black")
        RandomOfPlayers.place(x=z, y=270)
    pass

def RandomForNPC():
    npc = int(CountOfNPC.get())
    z = 0
    for i in range(npc):
        z = z + 40
        randomOut = secrets.randbelow(high - low) + low
        RandomOfNPC = tk.Label(window, text=randomOut, font=("Arial Bold", 15), fg="lime", bg="black")
        RandomOfNPC.place(x=z, y=375)
    pass

def RandomClear():
    clear1 = tk.Label(window, text= "                                                                                     ", font=("Arial Bold", 15), fg="lime", bg="black")
    clear1.place(x = 1, y = 270)
    clear2 = tk.Label(window, text="                                                                                   ", font=("Arial Bold", 15), fg="lime", bg="black")
    clear2.place(x = 1, y = 375)
    pass

def randomOutput():
    RandomClear()
    RandomForPlayers()
    RandomForNPC()


def XanIn():
    if XanBool.get() == 1:
        result = XanInit[iterator]
        incrementIterator()
        return result
    else:
        return 0

def incrementIterator():  # Increment iterator and reset to 0 if exceeded the list length
    global iterator
    iterator = (iterator + 1) % len(XanInit)


def Xanatar():
    players = int(CountOfPlayers.get())
    if XanBool.get() == 1:
        CountOfPlayers.delete(0,"end")
        CountOfPlayers.insert(0,5)
        for i in range(players):
            CPlayers = tk.Label(window, text = [x for x in XanPlayers], font=("Arial Bold", 10), fg="lime", bg="black")
            CPlayers.place(x=30, y=240)
    else:
        clear2 = tk.Label(window,
                          text="                                                                                   ",
                          font=("Arial Bold", 15), fg="lime", bg="black")
        clear2.place(x=30, y=240)


window = tk.Tk()

window.resizable(width=False, height=False)

window.title("DnD Random")

window.geometry('600x500')

window["bg"] = "black"

XanBool = tk.BooleanVar()

CPlayers = tk.Label(window, text = "Количество игроков", font = ("Arial Bold", 15), fg = "lime", bg = "black")
CPlayers.place(x = 1, y = 25)

CountOfPlayers = tk.Spinbox(from_=1.0, to = 10.0)
CountOfPlayers.place(x = 1, y = 65)

CNPC = tk.Label(window, text = "Количество NPC", font = ("Arial Bold", 15), fg = "lime", bg = "black")
CNPC.place(x = 1, y = 100)

presets = tk.Label(window, text = "Пресеты", font = ("Arial Bold", 10), fg = "lime", bg = "black")
presets.place(x = 400, y = 25)

preset = tk.Checkbutton(window, text = "Xanatar", variable= XanBool, offvalue= 0, onvalue=1, command= Xanatar, font = ("Arial Bold", 10), fg = "lime", bg = "black")
preset.place(x = 400, y = 50)

CountOfNPC = tk.Spinbox(from_=1.0, to = 10.0)
CountOfNPC.place(x = 1, y = 145)

CubesOfPlayers = tk.Label(window, text = "Кубы игроков", font = ("Arial Bold", 15), fg = "lime", bg = "black")
CubesOfPlayers.place(x = 1, y = 200)

CubesOfNPC = tk.Label(window, text = "Кубы NPC", font = ("Arial Bold", 15), fg = "lime", bg = "black")
CubesOfNPC.place(x = 1, y = 325)

btn = tk.Button(window, text = "Сгенерировать", command= randomOutput, font = ("Arial Bold", 15), fg = "black", bg = "white")
btn.place(x = 1, y = 425)


window.mainloop()