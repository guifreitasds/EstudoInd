#Importar Libs
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#CRIANDO JANELA

win = Tk()
win.title('DP SYSTEMS - Login - Acess Panel')
win.geometry("600x300")
win.configure(background="white")
win.resizable(width=False, height=False)


# CARREGANDO IMAGENS #
logo=PhotoImage(file="icons/logo.png")

# WIDGETS DA JANELA #
leftframe=Frame(win, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=LEFT)

rightframe=Frame(win, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
rightframe.pack(side=RIGHT)

logolabel=Label(leftframe, image=logo, bg="MIDNIGHTBLUE")
logolabel.place(x=50, y=100)


# Colocando o input de username
user=Label(rightframe, text="Username: ", font=("Century Gothic", 18), bg="MIDNIGHTBLUE", fg="white")
user.place(x=10, y=100)

userinput=ttk.Entry(rightframe, width=30)
userinput.place(x=150, y=110)

# Colocando o input de password
passw=Label(rightframe, text="Password: ", font=("Century Gothic", 18), bg="MIDNIGHTBLUE", fg="white")
passw.place(x=10, y=140)

passinput=ttk.Entry(rightframe, width=30)
passinput.place(x=150, y=150)

#Botão Login

logbutton=Button(rightframe, text="Login", width=20)
logbutton.place(x=120, y=210)

# Botão Register

regbutton=Button(rightframe, text="Register",width=20)
regbutton.place(x=120, y=240)

win.mainloop()
