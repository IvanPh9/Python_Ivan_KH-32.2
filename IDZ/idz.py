import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageDraw

# Оголошення кольорів
color = '#E3D1C4'
color_lb = '#E3D1C4'
color_button = '#E0C1A2'
color_red_bg = '#C17480'
color_blue_bg = '#97ABCA'
color_red_button = '#9F3B41'
color_blue_button = '#5B6E8C'
color_tx = '#30324A'
color_button_black = '#867461'
color_blue_black ='#364254'
color_red_black ='#5F2327'

# Глобальні змінні
root = tk.Tk() # Основне вікно гри
root.title("Tic Tac Toe") # Заголовок вікна
root.geometry('450x280') # Розміри вікна гри
root.configure(bg=color) # Налаштування фону вікна гри

board = [['', '', ''], ['', '', ''], ['', '', '']] # Ініціалізація поля гри
current_player = 'X' # Початковий гравець
moves = 0  # Лічильник ходів
timer_running = False # Флаг таймера
start_time = None # Час, коли таймер був запущений
win_x = 0 # Лічильник виграшів для гравця 'X'
win_o = 0 # Лічильник виграшів для гравця 'O'
buttons = [] # Список кнопок
timer_label = None # Елемент таймера
win_label = None # Елемент рахунку
title_label = None # Елемент заголовка
Picture = None # Елемент зображення фону
Diagrams = None # Елемент зображення діаграми

# Функція обробки ходу гравця
def make_move(row, col):
    global current_player, moves, timer_running, win_x, win_o

    if board[row][col] == '': # Перевірка, чи клітинка порожня
        board[row][col] = current_player
        buttons[row][col]['text'] = current_player
        # Зміна кольору кнопки в залежності від гравця
        if current_player == 'O':
            buttons[row][col]['bg'] = color_red_button
        else:
            buttons[row][col]['bg'] = color_blue_button
        moves += 1

        # Запуск таймера з першого ходу
        if moves == 1 and not timer_running:
            start_timer()

        # Перевірка на виграш
        if check_winner(current_player):
            stop_timer()
            tk.messagebox.showinfo('Game Over', f'Player {current_player} wins!') # виведення повідомлення про виграш
            if current_player == 'X': # ЗЗміна рахунку
                win_x += 1
            else:
                win_o += 1
            update_score() # Оновлення рахунку
            reset_game() # Скидання гри
        elif moves == 9: # Перевірка на нічию
            stop_timer()
            tk.messagebox.showinfo('Game Over', 'It\'s a draw!') # Виведення повідомлення про нічию
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X' # Зміна поточного гравця
            if current_player == 'X':
                root.configure(bg=color_blue_bg)  # Зміна фону для гравця X
                Diagrams_build(color_blue_bg)  # Оновлення діаграми для гравця X
                update_color(color_blue_bg) # Оновлення кольору інтерфейсу
            else:
                root.configure(bg=color_red_bg)  # Зміна фону для гравця O
                update_color(color_red_bg) # Оновлення діаграми для гравця O
                Diagrams_build(color_red_bg) # Оновлення кольору інтерфейсу

# Функція оновлення кольорів інтерфейсу
def update_color(color_i):
    global win_label, title_label, timer_label, Picture, current_player
    win_label['bg'] = color_i
    timer_label['bg'] = color_i
    title_label['bg'] = color_i
    # Зміна фону відповідно до кольору
    if color_i == color_red_bg:
        background_image = tk.PhotoImage(file="image_2.png")
        Picture['image'] = background_image
        Picture.image = background_image
    elif color_i == color_blue_bg:
        background_image = tk.PhotoImage(file="image_1.png")
        Picture['image'] = background_image
        Picture.image = background_image
    else:
        if current_player == 'X':
            background_image = tk.PhotoImage(file="bg_2.png")
            Picture['image'] = background_image
            Picture.image = background_image
        else:
            background_image = tk.PhotoImage(file="bg_1.png")
            Picture['image'] = background_image
            Picture.image = background_image

# Функція оновлення рахунку
def update_score():
    global win_label, win_x, win_o
    win_label['text'] = f'{win_x}:{win_o}'

def check_winner(player):
    # Перевірка по рядках
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Перевірка по стовпцях
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Перевірка по діагоналях
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Функція створення діаграми
def Diagrams_build(color_i):
    global win_x, win_o, Diagrams
    # Створюємо нове зображення діаграми з заданим фоном (color_i)
    img_d = Image.new("RGB", (60, 60), color_i)
    draw_d = ImageDraw.Draw(img_d)
    # Якщо є хоча б одна перемога, малюємо часткову кругову діаграму
    if win_o+win_x != 0:
        # Обчислюємо початковий кут для синьої частини (побудова відсотка перемог гравця X)
        start_i = (win_x*360)/(win_x+win_o)
        # Малюємо частину діаграми для гравця X (синій колір)
        draw_d.pieslice((10, 10, 50, 50), start=0, end=start_i, fill=color_blue_button, outline=color_blue_black)
        # Малюємо частину діаграми для гравця O (червоний колір)
        draw_d.pieslice((10, 10, 50, 50), start=start_i, end=360, fill=color_red_button, outline=color_red_black)
    else:
        # Якщо ще немає перемог, малюємо повний круг без поділу
        draw_d.ellipse((10, 10, 50, 50), fill=color_button, outline=color_button_black)
    # Зберігаємо зображення діаграми у файл "diagram_1.png"
    img_d.save("diagram_1.png")
    photo_d = tk.PhotoImage(file="diagram_1.png")
    # Оновлюємо зображення діаграми на елементі інтерфейсу
    Diagrams['image']= photo_d
    Diagrams.image = photo_d

# Функція запуску таймера
def start_timer():
    global timer_running, start_time
    timer_running = True # Позначаємо що тепер таймер працює
    start_time = time.time() # Зберігаємо час початку гри (відлік з поточного часу)
    # Викликаємо функцію для оновлення таймера
    update_timer()

# Функція зупинки таймера
def stop_timer():
    global timer_running
    # Зупиняємо таймер, коли гра завершується
    timer_running = False

# Функція оновлення часу на таймері
def update_timer():
    global timer_label, timer_running, start_time
    # Якщо таймер запущено, оновлюємо час
    if timer_running:
        elapsed_time = time.time() - start_time
        # Форматуємо час у вигляді "мм:сс"
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_str = f'{minutes:02d}:{seconds:02d}'
        timer_label['text'] = time_str
        # Викликаємо оновлення кожну секунду
        timer_label.after(1000, update_timer)

# Функція перезапуску гри
def reset_game():
    global board, current_player, moves, Picture, win_x, win_o
    # Очищаємо ігрове поле: створюємо нову порожню матрицю
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    # Визначаємо, хто буде починати гру:
    # Якщо перемог у гравця O більше або рівно ніж у гравця X, то починає X.
    if win_o >= win_x:
        current_player = 'X'
    else: current_player = 'O'
    # Скидаємо лічильник ходів
    moves = 0
    # Встановлюємо початковий колір фону для гри
    root.configure(bg=color)
    # Оновлюємо кольори елементів інтерфейсу
    update_color(color_lb)
    # Оновлюємо діаграму, яка відображає перемоги гравців
    Diagrams_build(color)
    # Очищаємо всі кнопки гри (середину поля) та скидаємо їхні кольори
    for row in buttons:
        for button in row:
            button['text'] = ''
            button['bg'] = color_button
    # Скидаємо таймер на початковий стан
    timer_label['text'] = '00:00'

# Основна функція
def main():
    global buttons, timer_label, win_label, title_label, Picture, Diagrams

    # Завантажуємо зображення фону
    background_image = tk.PhotoImage(file="image.png")
    Picture = tk.Label(image=background_image)
    Picture.image = background_image
    Picture.place(x=0, y =0)
    # Додаємо заголовок
    title_label = tk.Label(root, text="Tic Tac Toe", font=('Microsoft Himalaya', 28), bg=color_lb)
    title_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))
    # Створюємо діаграму перемог
    img = Image.new("RGB", (60, 60), color)
    draw = ImageDraw.Draw(img)
    draw.ellipse((10, 10, 50, 50), fill=color_button, outline='#867461')
    img.save("diagram.png")
    photo = tk.PhotoImage(file="diagram.png")
    Diagrams = tk.Label(root, image=photo, borderwidth=0)
    Diagrams.image = photo
    Diagrams.grid(row=2, column=4, rowspan=1, padx=20, pady=5)

    # Створюємо таймер гри
    timer_label = tk.Label(root, text='00:00', font=('Microsoft Himalaya', 18), padx=20, pady=5, bg=color_lb)
    timer_label.grid(row=1, column=3, rowspan=1, padx=20, pady=(10,0))
    # Створюємо елемент для відображення рахунку
    win_label = tk.Label(root, text=f'{win_x}:{win_o}', font=('Microsoft Himalaya', 18), bg=color_lb)
    win_label.grid(row=1, column=4, rowspan=1, padx=20, pady=(10,0))

    # Створюємо кнопки для гри
    for i in range(3):
        row = []  # Список для зберігання кнопок одного ряду
        for j in range(3):
            button = tk.Button(root, text='', font=('Microsoft Himalaya', 14), fg=color_tx,  bg=color_button, width=9, height= 3, command=lambda x=i, y=j: make_move(x, y), relief="ridge")
            if j == 0:
                button.grid(row=i+1, column=j, padx=(15, 0)) # Для першої колонки додаємо відступ
            else:
                button.grid(row=i + 1, column=j)
            row.append(button) # Додаємо кнопку до ряду
        buttons.append(row) # Додаємо ряд до загального списку кнопок

    root.mainloop() # Запускаємо основний цикл гри

if __name__ == '__main__':
    main()
