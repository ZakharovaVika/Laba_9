from tkinter import *
from tkinter import messagebox
import pickle
root = Tk()
root.title("Авторизация")
root.geometry("450x450+450+100")

main_label = Label(root, text="Войдите или зарегистрируйтесь", font="Arial 15 bold")
main_label.pack()

reg_usr_label = Label(root, text="Имя пользователя", font="Arial 11 bold", padx=10, pady=8)
reg_usr_label.pack()

reg_usr_ent = Entry(root, font='Arial 12')
reg_usr_ent.pack()

reg_pass_label = Label(root, text="Пароль", font="Arial 11 bold",padx=10, pady=12)
reg_pass_label.pack()

reg_pass_ent = Entry(root,show="*", font='Arial 12')
reg_pass_ent.pack()
btn = Button(root, text="Зарегистрироваться",padx=10, pady=3, command=lambda: info())
btn.pack()

def info():


    inf = {}
    inf[reg_usr_ent.get()] = reg_pass_ent.get()
    f = open("login.txt", "wb")
    pickle.dump(inf,f)
    f.close()
    if reg_usr_ent.get()!="" and reg_pass_ent.get()!="" :
        messagebox.showinfo("Регистрация","Вы успешно зарегистрировались!")
    else:
        messagebox.showerror("Ошибка","Введите логин и пароль")

usr_nme_lable = Label(root, text="Имя пользователя", font="Arial 11 bold", padx=10, pady=8)
usr_nme_lable.pack()

usr_ent = Entry(root, font='Arial 12')
usr_ent.pack()

pass_label = Label(root, text="Пароль", font="Arial 11 bold",padx=10, pady=8)
pass_label.pack()

pass_ent = Entry(root, show="*", font='Arial 12')
pass_ent.pack()

btn = Button(root, text="Войти", command=lambda :check())
btn.pack()

def check():

    if usr_ent.get()!= "":

        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if usr_ent.get() in a :
            if pass_ent.get() == a[usr_ent.get()]:
                messagebox.showinfo("Вход выполнен!","Вход выполнен")
                create()
            else:
                messagebox.showerror("Ошибка!","Неверный логин или пароль")
        else:
            messagebox.showerror("Ошибка!","Неверный логин")
    else:
        messagebox.showerror("Ошибка!", "Введите логи или пароль!")
def create():
    root.destroy()
    app = Tk()
    app.title("Игра")
    app.geometry("399x399+560+100")
    rows = cols = 10
    cells = 50
    canvas = Canvas(app, width=cells * rows, height=cells * cols)
    cell_colors = ['white', 'black']
    ci = 0  # color index
    for row in range(rows):
        for col in range(cols):
            x1, y1 = col * cells, row * cells
            x2, y2 = col * cells + cells, row * cells + cells
            canvas.create_rectangle((x1, y1), (x2, y2), fill=cell_colors[ci])

            ci = not ci

        ci = not ci

    canvas.pack()



root.mainloop()
