import tkinter as tk
from idlelib.colorizer import color_config
from tkinter import messagebox
import time
from PIL import Image, ImageDraw

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

# Global variables
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry('450x280')
root.configure(bg=color)

board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'
moves = 0
timer_running = False
start_time = None
win_x = 0
win_o = 0
buttons = []
timer_label = None
win_label = None
title_label = None
Picture = None
Diagrams = None

def make_move(row, col):
    global current_player, moves, timer_running, win_x, win_o

    if board[row][col] == '':
        board[row][col] = current_player
        buttons[row][col]['text'] = current_player
        if current_player == 'O':
            buttons[row][col]['bg'] = color_red_button
        else:
            buttons[row][col]['bg'] = color_blue_button
        moves += 1

        if moves == 1 and not timer_running:
            start_timer()

        if check_winner(current_player):
            stop_timer()
            tk.messagebox.showinfo('Game Over', f'Player {current_player} wins!')
            if current_player == 'X':
                win_x += 1
            else:
                win_o += 1
            update_score()
            reset_game()
        elif moves == 9:
            stop_timer()
            tk.messagebox.showinfo('Game Over', 'It\'s a draw!')
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            if current_player == 'X':
                root.configure(bg=color_blue_bg)
                Diagrams_build(color_blue_bg)
                update_color(color_blue_bg)
            else:
                root.configure(bg=color_red_bg)
                update_color(color_red_bg)
                Diagrams_build(color_red_bg)

def update_color(color_i):
    global win_label, title_label, timer_label, Picture
    win_label['bg'] = color_i
    timer_label['bg'] = color_i
    title_label['bg'] = color_i
    if color_i == color_red_bg:
        background_image = tk.PhotoImage(file="image_2.png")
        Picture['image'] = background_image
        Picture.image = background_image
    elif color_i == color_blue_bg:
        background_image = tk.PhotoImage(file="image_1.png")
        Picture['image'] = background_image
        Picture.image = background_image
    else:
        background_image = tk.PhotoImage(file="image.png")
        Picture['image'] = background_image
        Picture.image = background_image

def update_score():
    global win_label, win_x, win_o
    win_label['text'] = f'{win_x}:{win_o}'

def check_winner(player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def Diagrams_build(color_i):
    global win_x, win_o, Diagrams
    img_d = Image.new("RGB", (60, 60), color_i)
    draw_d = ImageDraw.Draw(img_d)
    if win_o+win_x != 0:
        start_i = (win_x*360)/(win_x+win_o)
        draw_d.pieslice((10, 10, 50, 50), start=0, end=start_i, fill=color_blue_button, outline=color_blue_black)
        draw_d.pieslice((10, 10, 50, 50), start=start_i, end=360, fill=color_red_button, outline=color_red_black)
    else:
        draw_d.ellipse((10, 10, 50, 50), fill=color_button, outline=color_button_black)
    img_d.save("diagram_1.png")
    photo_d = tk.PhotoImage(file="diagram_1.png")
    Diagrams['image']= photo_d
    Diagrams.image = photo_d

def start_timer():
    global timer_running, start_time
    timer_running = True
    start_time = time.time()
    update_timer()


def stop_timer():
    global timer_running
    timer_running = False


def update_timer():
    global timer_label, timer_running, start_time
    if timer_running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        time_str = f'{minutes:02d}:{seconds:02d}'
        timer_label['text'] = time_str
        timer_label.after(1000, update_timer)


def reset_game():
    global board, current_player, moves, Picture
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    moves = 0
    root.configure(bg=color)
    update_color(color_lb)
    Diagrams_build(color)
    for row in buttons:
        for button in row:
            button['text'] = ''
            button['bg'] = color_button
    timer_label['text'] = '00:00'


def main():
    global buttons, timer_label, win_label, title_label, Picture, Diagrams
    buttons = []
    background_image = tk.PhotoImage(file="image.png")
    Picture = tk.Label(image=background_image)
    Picture.image = background_image
    Picture.place(x=0, y =0)
    # Додаємо заголовок у верхньому рядку
    title_label = tk.Label(root, text="Tic Tac Toe", font=('Microsoft Himalaya', 28), bg=color_lb)
    title_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

    img = Image.new("RGB", (60, 60), color)  # Білий фон
    draw = ImageDraw.Draw(img)
    draw.ellipse((10, 10, 50, 50), fill=color_button, outline='#867461')
    img.save("diagram.png")
    photo = tk.PhotoImage(file="diagram.png")
    Diagrams = tk.Label(root, image=photo, borderwidth=0)
    Diagrams.image = photo
    Diagrams.grid(row=2, column=4, rowspan=1, padx=20, pady=5)

    # Розміщуємо таймер і рахунок збоку
    timer_label = tk.Label(root, text='00:00', font=('Microsoft Himalaya', 18), padx=20, pady=5, bg=color_lb)
    timer_label.grid(row=1, column=3, rowspan=1, padx=20, pady=(10,0))  # Розміщуємо таймер у стовпці 3

    win_label = tk.Label(root, text=f'{win_x}:{win_o}', font=('Microsoft Himalaya', 18), bg=color_lb)
    win_label.grid(row=1, column=4, rowspan=1, padx=20, pady=(10,0))  # Розміщуємо рахунок у стовпці 3

    # Створюємо кнопки для гри
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(root, text='', font=('Microsoft Himalaya', 14), fg=color_tx,  bg=color_button, width=9, height= 3, command=lambda x=i, y=j: make_move(x, y), relief="ridge")
            if j == 0:
                button.grid(row=i+1, column=j, padx=(15, 0))
            else:
                button.grid(row=i + 1, column=j)
            row.append(button)
        buttons.append(row)

    root.mainloop()

if __name__ == '__main__':
    main()