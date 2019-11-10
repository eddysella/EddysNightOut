from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to Story Creation")
window.resizable(height=None, width=None)


# create option class which is a frame and has list of options
# option has entry box left, combobox right on_press(set number of subOptions)
# create function which adds an option to list (add button below option)
# create function which removes an option from list (add button below option)
# create start button at top
# if time permits create save/load feature

class Option:
    frames = []
    widgets = []

    frames.append(Frame(window, borderwidth=2, relief="groove"))

    widgets.append(Entry(frames[0]))

    combo = Combobox(window)
    combo['values'] = [i for i in range(0, 101, 1)]
    widgets.append(combo)

    widgets[0].pack(side="left")
    widgets[0].pack(side="right")



def addOption():
    frame = Frame(window, borderwidth=2, relief="groove")
    frames.append(frame)

    frame.pack(side="top", fill="x")

    lbl = Label(window, text="Story:")
    lbl.grid(column=0, row=0)
    txt = Text(window, height=10, width=100)
    txt.grid(column=0, row=1)
    combo = Combobox(window)
    combo['values'] = [i for i in range(0, 101, 1)]
    combo.current(1)  # set the selected item
    combo.grid(column=1, row=1)
    btn = Button(window, text="Cl")

    for i in range(3):
        widget = Entry(frame)
        widgets.append(widget)

        widget.pack(side="left")


createWidgetButton = Button(window, text="Add Option", command=addOption)
createWidgetButton.pack(side="bottom", fill="x")

window.mainloop()
