#Importar Libs
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import databaser

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


def login_intosys():
    databaser.cursor.execute("""
    SELECT * FROM users
    WHERE (username=? and password=?)""", (userinput.get(), passinput.get()))
    verify=databaser.cursor.fetchone()
    try:
        if(userinput.get() in verify and passinput.get() in verify):
            messagebox.showinfo(title="Login INFO", message="Login sucessfull, Welcome!")
    except:
        messagebox.showerror(title="LoginERROR", message="Incorrect Credentials")


#Botão Login

logbutton=ttk.Button(rightframe, text="Login", width=20, command=login_intosys)
logbutton.place(x=120, y=200)

# Funções



def register_page():
    #Remover botões de página de login
    logbutton.place(x=5000)
    regbutton.place(x=5000)


    #Inserir botões de cadastro
    #Label do nome
    name=Label(rightframe, text="Name: ", font=("Century Gothic", 18), bg="MIDNIGHT BLUE", fg="white")
    name.place(x=10, y=30)
    #
    #Input do nome
    nameinput=ttk.Entry(rightframe, width=38)
    nameinput.place(x=100, y=40)
    #

    #Label do e-mail
    mail=Label(rightframe, text="E-mail: ", font=("Century Gothic", 18),bg="MIDNIGHT BLUE", fg="white")
    mail.place(x=10, y=65)
    #

    #Input do e-mail
    mailinput=ttk.Entry(rightframe, width=38)
    mailinput.place(x=100, y=75)
    #

    #Função de registrar na base de dados
    def register_intodb():
        #Pegando valores das entrys do tkinter
        name=nameinput.get()
        mail=mailinput.get()
        username=userinput.get()
        passw=passinput.get()

        if(name=="" and mail=="" and username=="" and passw=="" or name=="" and mail==""):
            messagebox.showerror(title="INSERTION DATA ERROR", message="Insert all the fields in this page")
        else:
            #Fazendo comandos SQL para inserção de dados
            databaser.cursor.execute("""
            INSERT INTO users(name, mail, username, password)
            VALUES(?, ?, ?, ?)""", (name, mail, username, passw))
            databaser.conn.commit()
            messagebox.showinfo(title="REGISTER INFO", message="Register sucessfull")


    #Botões da página de registro
    regbutton_inregpage=ttk.Button(rightframe, text="Register", width=20, command=register_intodb)
    regbutton_inregpage.place(x=120, y=220)
    #
    

    def go_back():
        #Removendo widgets de cadastro
        name.place(x=5000)
        nameinput.place(x=5000)
        mail.place(x=5000)
        mailinput.place(x=5000)
        backbutton.place(x=5000)
        regbutton_inregpage.place(x=5000)

        #Voltando com a tela de login
        logbutton.place(x=120, y=200)
        regbutton.place(x=135, y=230)
    
    backbutton=ttk.Button(rightframe, text="Go back", width=15, command=go_back)
    backbutton.place(x=135,y=250)


# Botão Register

regbutton=ttk.Button(rightframe, text="Register",width=15, command=register_page)
regbutton.place(x=135, y=230)


win.mainloop()
