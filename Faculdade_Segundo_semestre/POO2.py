# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe

'''
class A:
    def __new__(cls,x):
        print('before make instances')
        instancia =  super().__new__(cls)
        print('After')
        return instancia

    def __init__(self,x):
        self.x = x
        print('I am init', self.x)

    def __repr__(self):
        return 'A()'
    
a = A(123)
print(a)'''

#CONTEXT MANAGER
'''
class MyOpen:
    def __init__(self, cam_arq, mode):
        self.cam_arq = cam_arq
        self.mode = mode
        self._arquivo = None

    def __enter__(self):
        print('ENTER')
        self._arquivo = open(self.cam_arq, self.mode, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_execption, exception_, traceback):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('Minha nota')

        # return True  # Tratei a exceção

instancia= MyOpen('POO2.txt', 'w')
with instancia as arquivo:
    arquivo.write('Hi\n')
    arquivo.write('test')
    print('WITH', arquivo)

'''
#Decorators(@). Evite a herança e prefira a conveção, usando a function add_repr ao inves do MyReprMixin
'''
def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls
#Decorador de metodos para evitar uma recursão referente ao metodo "falar_nome"
def my_planet(method):
    def intern(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        if 'Terra' in result:
            return 'you here in house'
        return result
    return intern


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    
@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
    
@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    @my_planet
    def falar_nome(self):
       return f'O planeta é: {self.nome}'

br = Time('Brasil')
pt = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')
print(br)
print(pt)
print(terra.falar_nome())
print(marte.falar_nome())
'''

# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
''' 
from typing import Any

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 1234
    
call = CallMe('11555555')
ret = call('Andrei Kwok')
print(ret)
'''

# Classes decoradoras (Decorator classes)
'''
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(2)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
'''
# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# object acima
# class Foo:
#     ...

'''
Foo = type('Foo', (object,), {})
f = Foo()
# print(isinstance(f, Foo))
print(type(f))
print(type(Foo))
'''

#EXEMPLO DA METACLASSE
''' 
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr
        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia
    
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('FALANDO...')

p1 = Pessoa('Andrei')
print(p1.attr)
print(p1)
p1.falar()
'''
########################################################################################################################
# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

'''from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    print(p1 == p2)'''

'''from dataclasses import dataclass


@dataclass
@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self):
        print('POST INIT')

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(p1.nome_completo)'''

# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
'''from dataclasses import dataclass
from dataclasses import asdict, astuple, dataclass


@dataclass(repr=True)
@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])'''

'''from dataclasses import dataclass, field, fields

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
    p1 = Pessoa()
    # print(fields(p1))
    print(p1)'''

# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple

'''from collections import namedtuple

Carta = namedtuple('Carta', ['valor','naipe'])
as_espadas = Carta('A', 'Espadas')
print(as_espadas._asdict()) #retorna um dicionario
print(as_espadas.naipe)
print(as_espadas.valor)
print(as_espadas._fields)
print(as_espadas._field_defaults)
from typing import NamedTuple

#EXEMPLO !=
class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A')
print(as_espadas._asdict())'''

# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

'''from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')'''