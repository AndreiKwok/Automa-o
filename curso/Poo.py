''' @property e setter

class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa) 
'''
'''ATRIBUTOS Privados e protegidos
class Public:
    def __init__(self, cpf, rg):
        self.__private_cfp = cpf
        self.__private_rg = rg
        self._protected_cfp = cpf
        self._protected_rg = rg
        #print('Metodo privado', self.__private_cfp, self.__private_rg)

    def get_private(self):
        return'Metodo privado', self.__private_cfp, self.__private_rg)

    def get_protected(self):
        return f'{self._protected_cfp}\n{self._protected_rg}'

class Protected(Public):
    def __init__(self, cpf, rg):
        super().__init__(cpf, rg)
        return ('Metodo protegido', self._protected_cfp, self._protected_rg)
    
P = Protected(1711111, 55555)
#itens privados sempre serão restritos as classes declaradas
#já protegidos é possivel utilizar com base na herança, porém não é recomendavel
'''
'''# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
print(f.metodo_publico())
'''

#ex sobre POO
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}\nANO:{self.ano}'

class Motor(Carro):
    def __init__(self, marca, modelo, ano, motor):
        super().__init__(marca, modelo, ano)
        self.motor = motor
    
    def __str__(self):
        return f'{super().__str__()}\nMOTOR:{self.motor}'
    
class Fabricante(Motor):
    def __init__(self, marca, modelo, ano, motor, fabricante):
        super().__init__(marca, modelo, ano, motor)
        self.fabricante = fabricante

    def __str__(self):
        return f'{super().__str__()}\nFABRICANTE:{self.fabricante}'

c1 = Fabricante('volks', 'POLO', 2023, '500CV', 'volks')
car = c1.__str__()
print(str(car).strip('(').strip(')'))
help(Fabricante)