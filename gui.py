from tkinter import*
from PIL import Image , ImageTk
import action 
import spech_to_text 
from pathlib import Path
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
import  tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

cwd = os.getcwd()
pth = rf"{cwd}\image"

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(pth)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    entry_2.insert(END, "User: "+send+"\n")
    if bot != None:
        entry_2.insert(END, "Bot: "+ str(bot)+"\n")
    if bot == "Olá":
          window.destroy()

def ask():

    ask_val= spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    entry_2.insert(END, "User: "+ask_val+"\n") 
    if bot_val != None:
       entry_2.insert(END, "Bot: "+ str(bot_val)+"\n")
    if bot_val == "Olá":
        window.destroy()

window = tk.Tk()
sc_w = window.winfo_screenwidth()
sc_h = window.winfo_screenheight()
app_h = int(sc_h*0.9)
app_w = int(sc_w*0.7)
app_w_m = int((sc_w/3.5)/2)

# print(sc_w)
# print(sc_h)
wg = window.geometry(f"{int(sc_w/3.5)}x{app_h}+{app_w}+{int(sc_h*0.01)}")
window.configure(bg = "#17224D")

# print(f"{app_w},{app_h}")


canvas = Canvas(
    window,
    bg = "#17224D",
    height = 852,
    width = 393,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    393.0,
    852.0,
    fill="#17224D",
    outline="")

canvas.create_rectangle(
    0.0,    
    326.0,
    393.0,
    852.0,
    fill="#0C2279",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    app_w_m,
    app_h/1.7,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    app_w_m,
    app_h*(0.3),
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    app_w_m,
    app_h - 220,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    163.0,
    app_h - 77,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= ask,
    relief="flat",
    bg="#1837AF",
    activebackground="#1837AF"


)
button_1.place(
    x=101.0,
    y= app_h - 50,
    width=190.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= User_send,
    relief="flat",
    bg="#1837AF",
    activebackground="#1837AF"
)
button_2.place(
    x=324.0,
    y=app_h - 100,
    width=62.0,
    height=45.0
)

# entry_image_1 = PhotoImage(
#     file=relative_to_assets("entry_1.png"))
# entry_bg_1 = canvas.create_image(
#     169.0,
#     762.0,
#     image=entry_image_1
# )

# Entry barra de baixo
entry1 = Entry(
    window,
    justify = LEFT,
    bd=0,
    bg="#F8F1F2",
    # bg="#444444",
    font= ('Arial 16 bold'),
    fg="#001EE0",
    highlightthickness=0)

entry1.place(
    x=21.0,
    y=app_h - 98,
    width=296.0,
    height=40.0
)

# entry_1 = Entry(
#     bd=0,
#     # bg="#F8F1F2",
#     bg="#444444",
#     fg="#001EE0",
#     highlightthickness=0
# )
# entry_1.place(
#     x=21.0,
#     y=app_h - 98,
#     width=296.0,
#     height=40.0
# )

# entry_image_2 = PhotoImage(
#     file=relative_to_assets("entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     196.5,
#     606.0,
#     image=entry_image_2
# )

#Entry texto AI

entry_2 = Text(
    window,
    bd=0,
    bg="#1837BF",
    fg="#FFFFFF",
    font= ('Arial 12'),
    highlightthickness=0,     
)

entry_2.grid(row = 2,  column= 0)

entry_2.place(
    x=28.0,
    y=app_h/2.2,
    width=337.0,
    height=275.0
)
window.resizable(True,True)
window.mainloop()
