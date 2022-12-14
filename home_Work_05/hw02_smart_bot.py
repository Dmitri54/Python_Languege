import random
from tkinter import *
from tkinter import messagebox


def clicked(index):
    global name
    name = '{}'.format(ent[index].get())
    if name.replace(' ', '') != '':
        ent[index].config(state='disabled')


def begin():
    global amount
    global go
    go = random.randint(0, 1)
    if name == '':
        messagebox.showinfo('', 'Введите имя')
    else:
        amount = 2021
        ent[2].config(state='normal')
    if go == 1:
        amount -= bot()
    else:
        txt_3.config(text='')
    txt_0.config(text=f'Осталось: {amount} конфет(ы)')


def steps():
    global go
    global amount
    try:
        amount -= player_step()
    except TypeError:
        return
    if amount < 1:
        messagebox.showinfo('Победа', 'Ура - победа!')
    else:
        step = bot()
        amount -= step
        if amount < 1:
            messagebox.showinfo('Game over', 'Bot win!')
    txt_0.config(text=f'Осталось: {amount} конфет(ы)')


def player_step():
    global amount
    global go
    try:
        step = int('{}'.format(ent[2].get()))
        if 0 < step < 29:
            amount -= step
            txt_0.config(text=f'Осталось: {amount} конфет(ы)')
            return step
        else:
            messagebox.showinfo('', 'За ход можно забрать не более чем 28 конфет.')
    except ValueError:
        messagebox.showinfo('', 'Введите число.')


def bot():
    global amount
    if amount % 29 == 0:
        step = random.randint(1, 28)
    else:
        step = amount % 29
    txt_0.config(text = f'Осталось: {amount} конфет(ы)')
    txt_3.config(text = f'Bot взял {step}: конфет')
    return step


window = Tk()
window.title('Игра в конфеты против умного бота')


ent = [Entry(width = 26) for i in range(2)]
ent[0].grid(row = 1, column = 0)
ent.append(Entry(width = 26, state ='disabled'))

ent[2].grid(row = 9)

ent[0].focus()

btn = [Button(text ='Введите имя игрока', width = 20,
              command = lambda j = i: clicked(j)) for i in range(2)]
btn[0].grid(row = 1, column = 1)

btn_2 = Button(text ='Взять конфеты', width = 20, command = steps)
btn_2.grid(row = 9, column = 1)
btn_3 = Button(text = 'Начать', width = 35, command = begin)
btn_3.grid(row = 6, columnspan = 2)


amount = 2021
go = random.randint(0, 1)
name = ''


txt_0 = Label(text = f'Осталось: {amount} конфет(ы)')
txt_0.grid(row = 7, column = 0)

txt_2 = Label()
txt_2.grid(row = 5)
txt_3 = Label(justify = LEFT)
txt_3.grid(row = 10)


window.mainloop()
