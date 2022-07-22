from tkinter import *

fuse = 100
score = 0
can_start = True

my_font = ('Comic Sans MS', 14)


def start(event):
    print("start")
    global can_start, fuse, score
    if can_start:
        fuse = 100
        score = 0
        main_label.config(text='')
        update_bomb()
        update_display()
        can_start = False


def update_display():
    print("update display")
    global fuse, score
    if fuse > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < fuse <= 50:
        bomb_label.config(image=danger_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text='Fuse: ' + str(fuse))
    score_label.config(text='Score: ' + str(score))
    fuse_label.after(100, update_display)


def update_bomb():
    global fuse
    fuse -= 5
    print("fuse: ", fuse)
    if is_alive():
        fuse_label.after(400, update_bomb)


def click():
    print("click!")
    global score
    if is_alive() and not can_start:
        score += 1
        print("score: ", score)


def is_alive():
    global fuse, can_start
    if fuse <= 0:
        main_label.config(text='Bang! Bang! Bang!')
        can_start = True
        return False
    else:
        return True


root = Tk()
root.title('Bang Bang')
root.geometry('500x550')

main_label = Label(text='Press [enter] to start the game', font=my_font)
main_label.pack()

fuse_label = Label(text='Fuse: ' + str(fuse), font=my_font)
fuse_label.pack()
score_label = Label(text='Score: ' + str(score), font=my_font)
score_label.pack()

danger_photo = PhotoImage(file='img/bomb_no.gif')
normal_photo = PhotoImage(file='img/bomb_normal.gif')
bang_photo = PhotoImage(file='img/pow.gif')

bomb_label = Label(image=normal_photo)
bomb_label.pack()

click_button = Button(text='Click me', font=my_font, command=click)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()
