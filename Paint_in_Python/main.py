from tkinter import*

canvas_width = 700 # размер окна для рисования
canvas_height = 500

brush_size = 3 # Размер кисти
color = "black"

def paint(event): 
    global brush_size
    global color
    x1 = event.x - brush_size 
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color) # Рисовать буду овалом, т.к. кисть

def brish_size_change(new_size): # Смена размера
    global brush_size
    brush_size = new_size

def color_change(new_color): # Смена цвета
    global color
    color = new_color


root = Tk()
root.title("Paint на Питоне")

w = Canvas(root, 
           width=canvas_width,
           height=canvas_height,
           bg="white") # Область рисования

w.bind("<B1-Motion>", paint) # Следовать за мышкой, при нажатии на левую кнопку (B1) мыши. 

# Создал кнопки для цвета:
red_btn = Button(text="Красный", width=10, command=lambda: color_change("red"))
blue_btn = Button(text="Синий", width=10, command=lambda: color_change("blue"))
black_btn = Button(text="Чёрный", width=10, command=lambda: color_change("black"))
white_btn = Button(text="Ластик", width=10, command=lambda: color_change("white"))

clear_btn = Button(text="Удалить всё", width=10, command=lambda: w.delete("all"))

# Кнопки изменения размера кисти:
one_btn = Button(text="2", width=10, command=lambda: brish_size_change(2))
five_btn = Button(text="5", width=10, command=lambda: brish_size_change(5))
ten_btn = Button(text="Десять", width=10, command=lambda: brish_size_change(10))
twelve_btn = Button(text="Двенадцать", width=10, command=lambda: brish_size_change(12))
twenty_btn = Button(text="Пятнадцать", width=10, command=lambda: brish_size_change(15))

w.grid(row=2, column=0, 
       columnspan=7, padx=5, 
       pady=5, sticky=E+W+S+N)

w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

# Вставлю кнопки изменения цвета:
red_btn.grid(row=0, column=2) 
blue_btn.grid(row=0, column=3)
black_btn.grid(row=0, column=4)
white_btn.grid(row=0, column=5)
clear_btn.grid(row=0, column=6, sticky=W)

# Вставлю кнопки изменения размера:
one_btn.grid(row=1, column=2)
five_btn.grid(row=1, column=3)
ten_btn.grid(row=1, column=4)
twelve_btn.grid(row=1, column=5)
twenty_btn.grid(row=1, column=6, sticky=W)

root.mainloop() # Создал окно