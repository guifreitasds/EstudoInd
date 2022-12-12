# Prof. Cloves Rocha
# Aula Prática: Herança e Polimorfismo
# Polimorfismo - Code 1

class Animal(): # Criando classe animal
        def __init__(self, nome, peso): # método construtor
          self.__nome = nome
          self.__peso = peso
        def __str__(self): # Metodo ToString
            return 'Nome: %s \nPeso: %f' % (self.__nome, self.__peso)
        def __gt__(self, other):
            return self.__peso > other.__peso
        def __add__(self, other):
          return Animal(self.__nome + ', ' + other.__nome, self.__peso + other.__peso)
          
        def alimentar(self, comida):
              self.__peso += comida
        
        @property
        def nome(self):
                return self.__nome
        @nome.setter
        def nome(self, new_name):
                  if type(new_name) == type(str()):
                          self.__nome = new_name


# Polimorfismo - Code 2 desenvolva o restante no desafio...
# from Animal import Animal
class Mamifero(Animal):
    classe = 'Mamifero'

    def __str__(self):
        return super().__str__() + 'Mamifero'

if __name__ == '__main__':
    animal1=Animal("Cobra", 5)
    print(animal1.alimentar(2))