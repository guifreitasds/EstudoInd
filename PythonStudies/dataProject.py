# Cadastro, pesquisa e exclusão de nomes

from ast import Delete
from atexit import register


clients = []

def registerClients():
    for i in range(0, 100000):
        sure = (float(input("Tem certeza que deseja adicionar um novo cliente? 1 - Sim / 2 - Não ")))
        if sure == 2:
          break

        elif sure == 1:
          clients1 = (str(input("Escreva o nome do cliente: ")))
          clients.append(clients1)
          print(clients)

def searchClients():
    search = str(input("Escreva o nome do cliente a ser pesquisado: "))
    if search in clients:
        print("Cliente encontrado!")
    else:
        print("Cliente não encontrado")

def deleteClients():
    clientDelete = str(input("Escreva o nome do cliente a ser deletado: "))
    if clientDelete in clients:
        clients.remove(clientDelete)
        print(clients)
    else:
        print("Cliente não encontrado")
    


while True:
  chooseMenu = float(input("1 - Cadastro de clientes / 2 - Pesquisa de clientes / 3 - Excluir clientes / 4 - Sair "))

  if chooseMenu == 1:
    registerClients()
  elif chooseMenu == 2:
    searchClients()
  elif chooseMenu == 3:
    deleteClients()
  elif chooseMenu == 4:
    break


        