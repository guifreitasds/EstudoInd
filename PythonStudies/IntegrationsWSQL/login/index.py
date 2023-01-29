#Importar Libs
from tkinter import *
from tkinter import messagebox

#CRIANDO JANELA

win = Tk()
win.title('GRINGOTTS Login - Acess Panel')
win.geometry("600x300")
win.configure(background="white")
win.resizable(width=False, height=False)


# WIDGETS DA JANELA #
leftframe=Frame(win, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=LEFT)

rightframe=Frame(win, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
rightframe.pack(side=RIGHT)

win.mainloop()
