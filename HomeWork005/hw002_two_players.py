# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# ======================================================================================================

import random
from tkinter import*
from tkinter import messagebox


def clicked(index):
    global name
    name[index] = '{}'.format(ent[index].get())
    if name[index].replace(' ', '') != '':
        ent[index].config(state='disabled')


def begin():
    global amount
    if name[0] == '' or name[1] == '':
        messagebox.showinfo('Введите имена игроков')
    else:
        amount = 2021
        txt_1.config(text=f'Ходит: {name[go]}')
        txt_0.config(text=f'Осталось: {amount} конфет(ы)')
        ent[2].config(state='normal')


def player_step():
    global amount
    global go
    try:
        step = int('{}'.format(ent[2].get()))
        if 0 < step < 29:
            amount -= step
            txt_0.config(text=f'Осталось: {amount} конфет(ы)')
            txt_3.config(text=f'{name[go]} взял(а) {step}: конфет')
            if amount < 1:
                messagebox.showinfo('The end', f'Победил(а) {name[go]}')
            if go == 0:
                go = 1
            else:
                go = 0
            txt_1.config(text=f'Ходит: {name[go]}')
        else:
            messagebox.showinfo('За ход можно забрать не более чем 28 конфет.')
    except ValueError:
        messagebox.showinfo('Введите число.')


window = Tk()
window.title('Игра в конфеты на двоих')


ent = [Entry(width=26) for i in range(2)]
ent[0].grid(row=1, column=0)
ent[1].grid(row=2, column=0)
ent.append(Entry(width=26, state='disabled'))

ent[2].grid(row=9)

ent[0].focus()

btn = [Button(text='Введите имя игрока', width=20, command=lambda j=i: clicked(j)) for i in range(2)]
btn[0].grid(row=1, column=1)
btn[1].grid(row=2, column=1)

btn_2 = Button(text='Взять конфеты', width=20, command=player_step)
btn_2.grid(row=9, column=1)
btn_3 = Button(text='Начать', width=35, command=begin)
btn_3.grid(row=6, columnspan=2)


amount = 2021
go = random.randint(0, 1)
name = [''] * 2

txt_0 = Label(text=f'Осталось: {amount} конфет(ы)')
txt_0.grid(row=7, column=0)
txt_1 = Label()
txt_1.grid(row=8)
txt_2 = Label()
txt_2.grid(row=5)
txt_3 = Label(justify=LEFT)
txt_3.grid(row=10)


window.mainloop()