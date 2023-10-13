from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file(): # Создаю новую заметку
    global file_menu 
    file_name = "Без названия"
    text.delete('1.0', END) # Удаляю все заметки, которые были ранее.

def save_as(): # Сохраняю заметку
    out = asksaveasfile(mode = 'w', defaultextension = '.txt')
    data = text.get('1.0', END)
    try: 
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Ой!", "нельзя сохранить фаил!")

def open_file(): # Открываю заметку
    global file_name
    inp = askopenfile(mode = 'r')
    if inp is None:
        return 
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = Tk()
root.title("Заметки")
root.geometry("400x400")

text = Text(root, width=400, height=400) # создал поле текст. 
text.pack()

menu_bar = Menu(root) # содержит значение всего меню
file_menu = Menu(menu_bar)

file_menu.add_command(label = "Новый", command = new_file)
file_menu.add_command(label = "Открыть", command = open_file)
file_menu.add_command(label = "Сохранить как", command = save_as)

menu_bar.add_cascade(label = "Фаил", menu = file_menu)

root.config(menu = menu_bar)
root.mainloop()
