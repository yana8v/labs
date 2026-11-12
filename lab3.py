import tkinter as tk # графический интерфейс
import random 
import pygame # музыка


def generate_key():
    first = random.randint(1, 26)
    last = random.randint(1, 26)
    if first > last: # поменять местами если первое больше второго
        temp = first # временная переменная для обмена числами
        first = last
        last = temp

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = '' # просто пустая строка в которую потом будут записываться буквы

    for i in range(first-1, last): # создание диапазона букв
        letters += alphabet[i]

    middle = ''
    for i in range(7): # сами 7 букв в центре пароля
        number = random.randint(0, len(letters) - 1)
        middle += letters[number]

    first = str(first) # превращение чисел в строку чтобы их можно было
    last = str(last) # использовать в одном тексте вместе с буквами

    if len(first) == 1: # проверка длины строки
        first = '0' + first
    if len(last) == 1:
        last = '0' + last

    key = first + ' ' + middle + ' ' + last

    key_field.delete(0, 'end') # удаление 
    key_field.insert(0, key) # новый пароль


def blink_title(): # мигание заголовка
    if title['fg'] == 'white':
        title.config(fg='#c69b55')
    else:
        title.config(fg='white')

    window.after(500, blink_title)


def update_loading(): # загрузка
    global progress
    progress += 10
    if progress > 180:
        progress = 180

    loading_bar.coords(loading_line, 0, 0, progress, 5)

    if progress < 180:
        window.after(122, update_loading)


def finish_loading(): # конец загрузки
    loading_screen.destroy()
    blink_title()


def close_app(): # закрытие программы
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    window.destroy()


window = tk.Tk() # главное окно
window.title('CS2 KEYGEN') # название и размер окна
window.geometry('1000x625')
window.resizable(0, 0) # запрет на изменение размера окна
bg_img = tk.PhotoImage(file='cs2_background.png') # фоновое изображение
label_bg = tk.Label(window, image=bg_img) # виджет с изображением
label_bg.place(x=0, y=0, relwidth=1, relheight=1) # чтобы оно было во все окно


panel = tk.Frame( # центральная панель
    window,
    bg='#202020',
    width=430,
    height=235
)
panel.place(relx=0.5, rely=0.5, anchor='center') # расположение панели

title = tk.Label( # заголовок
    panel,
    text='CS2 KEYGEN',
    font=('Arial', 22, 'bold'),
    bg='#202020',
    fg='white'
)
title.place(relx=0.5, y=40, anchor='center') # расположение заголовка

key_field = tk.Entry( # поле для пароля
    panel,
    font=('Arial', 16),
    justify='center',
    bg='#333333',
    fg='white',
    insertbackground='white',
    width=25
)
key_field.place(relx=0.5, y=110, anchor='center') # расположение его

generate_button = tk.Button( # кнопка
    panel,
    text='GENERATE KEY',
    font=('Arial', 12, 'bold'),
    bg='#c69b55',
    fg='black',
    width=20,
    command=generate_key
)
generate_button.place(relx=0.5, y=165, anchor='center')

loading_screen = tk.Frame(window, bg='#202020') # экран загрузки поверх
loading_screen.place(x=0, y=0, relwidth=1, relheight=1)

loading_title = tk.Label( # заголовок экрана загрузки
    loading_screen,
    text='CS2 KEYGEN',
    font=('Arial', 28, 'bold'),
    bg='#202020',
    fg='white'
)
loading_title.place(relx=0.5, rely=0.43, anchor='center')

loading_text = tk.Label( # надпись загрузки
    loading_screen,
    text='INITIALIZING...',
    font=('Arial', 10),
    bg='#202020',
    fg='#c69b55'
)
loading_text.place(relx=0.5, rely=0.51, anchor='center')

loading_bar = tk.Canvas( # полоска загрузки
    loading_screen,
    width=180,
    height=5,
    bg='#333333',
    highlightthickness=0
)
loading_bar.place(relx=0.5, rely=0.55, anchor='center')

loading_line = loading_bar.create_rectangle( # пустая линия загрузки
    0, 0, 0, 5,
    fill='#c69b55',
    outline=''
)


pygame.mixer.init() # музыка
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


progress = 0 # начальное значение загрузки
update_loading() # запускаем заполнение полоски
window.after(5500, finish_loading) # через 5,5 секунд конец загрузки
window.protocol('WM_DELETE_WINDOW', close_app) # функция для закрытия окна

window.mainloop()
