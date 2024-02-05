
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("")
root.geometry("800x800")

canvas = Canvas(root, width=600 , height = 500, highlightbackground = "gray", background = "gray")
canvas.place(relx = 0.5, rely = 0.4, anchor = CENTER)


coordinates_value = [10,50,100,200,300,400,500,600,700,800,900]
d1 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d1.place(relx = 0.2, rely=0.8, anchor = CENTER)
d2 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d2.place(relx = 0.4, rely=0.8, anchor = CENTER)
d3 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d3.place(relx = 0.6, rely=0.8, anchor = CENTER)
d4 = ttk.Combobox(root, state = "readonly", values = coordinates_value, width = 10)
d4.place(relx = 0.85, rely=0.8, anchor = CENTER)

startx = Label(root, text = "Startx :").place(relx =0.1 , rely =0.8 , anchor = CENTER)

starty = Label(root, text = "Starty :").place(relx =0.3 , rely =0.8 , anchor = CENTER)


Endx = Label(root, text = "Endx :").place(relx =0.5 , rely = 0.8, anchor = CENTER)


Endy = Label(root, text = "Endy :").place(relx =0.7 , rely = 0.8, anchor = CENTER)
Choose_Colour = Label(root, text = "Choose Colour").place(relx = 0.7 , rely = 0.9, anchor = CENTER)
fillcolours = ["Green", "Yellow", "Blue", "Red"]
colour_drop = ttk.Combobox(root, state = "readonly", values = fillcolours, width = 10)
colour_drop.place(relx = 0.85, rely = 0.9, anchor = CENTER)

def circle (Event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress  = "c"
    draw(keypress, oldx,oldy,newx,newy)   
    
def draw(keypress, oldx,oldy,newx,newy):
    colour =  colour_drop.get






root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<L>", line)




root.mainloop()