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
win.iconbitmap(default="icons/LogoIcon.ico")

#Adicionando transparência
win.attributes("-alpha", 0.95)


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

passinput=ttk.Entry(rightframe, width=30, show="•")
passinput.place(x=150, y=150)

#Botão Login

logbutton=ttk.Button(rightframe, text="Login", width=20)
logbutton.place(x=120, y=200)

# Funções

def register():
    #Remover botões de página de login
    logbutton.place(x=5000)
    regbutton.place(x=5000)
    user.place(x=5000)
    userinput.place(x=5000)
    passw.place(x=5000)
    passinput.place(x=5000)

    #Inserir botões de cadastro
    #Label do nome
    name=Label(rightframe, text="Name: ", font=("Century Gothic", 18), bg="MIDNIGHT BLUE", fg="white")
    name.place(x=10, y=20)
    #
    #Input do nome
    nameinput=ttk.Entry(rightframe, width=30)
    nameinput.place(x=100, y=30)
    #

    #Label do e-mail
    mail=Label(rightframe, text="E-mail: ", font=("Century Gothic", 18),bg="MIDNIGHT BLUE", fg="white")
    mail.place(x=10, y=55)

    #Input do e-mail
    mailinput=ttk.Entry(rightframe, width=30)
    mailinput.place(x=100, y=65)

    #Botões da página de registro
    regbutton_inregpage=ttk.Button(rightframe, text="Register", width=20)
    regbutton_inregpage.place(x=120, y=220)
    backbutton=ttk.Button(rightframe, text="Go back", width=15)
    backbutton.place(x=135,y=250)

# Botão Register

regbutton=ttk.Button(rightframe, text="Register",width=15, command=register)
regbutton.place(x=135, y=230)

win.mainloop()
