#Polimorfismo e assinatura de method
#assinatura de method = mesmo nome e quantidade de param

''' 
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg
    @abstractmethod
    def enviar(self) -> bool:...

class NotifyEmail(Notificacao):
    def enviar(self):
        print(f'EMAIL ENVIADO, {self.msg}')
        return True

class NotifySMS(Notificacao):
    def enviar(self):
        print(f'sms ENVIADO, {self.msg}')
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')

    else: print(print('Notificação não enviada'))


e = NotifyEmail('testeeee')
e.enviar()
notificar(e)
s = NotifySMS('testeeee')
s.enviar()
notificar(s)
'''
''' @classmethod 
#metodos de classe. são metodos onde "self" será "cls"
# ao inves de receber a instancia no primeiro parametro, receberemos a propria classe

class People:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @classmethod
    def return_dados(cls, nome, idade, cpf):
        re = f'Olá, {nome}. Segue os seus dados: \n'\
        f'idade: {idade}\n'\
        f'CPF: {cpf}'
        return re
    
    @classmethod
    def valida_idade(cls, idade):
        if idade >= 18:
            return 'Maior de idade'
        else:
            return 'Menor de idade'


p1 = People.return_dados('Boninho', 22, 4445559933)
p = People.valida_idade(17)
print(p1)
print(p)
'''
''' @staticmethod 
# @staticmethod (metodos estaticos) são inuteis
# Métodos estáticos são met que estão dentro da classe, mas não tem acesso ao self e cls
# em resumo, são funções que existem dentro da sua classe

class Classe:
    @staticmethod
    def function(*args, **kwargs):
        print('oi', args, kwargs)

c1 = Classe
Classe.function(1, 2, 3, nomeado='777')
'''
''' GETTERS
class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor
    
    def get_cor(self):
        return self.cor_tinta
    
caneta = Caneta('BANA')
print(caneta.get_cor())
'''
''' SETTERS
class Conta:
    def __init__(self, email, cpf):
        self.email_client = email
        self.cpf_client = cpf
    
    def set_client(self, email, cpf):
        self.email_client = email
        self.cpf_client = cpf

        return f'Dados atualizandos.\n'\
                f'EMAIL: {self.email_client}'\
                f'CPF: {self.cpf_client}'
    
    def get_client(self):
        return self.email_client, self.cpf_client
    
c1 = Conta('fernanadeskwok@gmail.com', 5555555)
c2 = c1.set_client('josafa@gmail.com', 9999999)
print(c2.get_client())
'''
''' @property
# @property funciona comno getter
class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor
    @property
    def cor_teste(self):
        return self.cor_tinta

caneta = Caneta('vermelho')
print(caneta.cor_teste)
'''
''' LOG
from mixin import LogPrintMixin
class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if not self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self._nome} LIGADO'
            self.log_sucess(msg)
    
    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} DESLIGADO'
            self.log_error(msg)
    
a = Smartphone('Android')
ios = Smartphone('Iphone')
a.ligar()
ios.desligar()
'''

#CLASS ABTRATAS  (ABC)
#Não da para instanciar a classe utilizando o ABC method
'''
from abc import ABC, abstractmethod
class Log(ABC):
    @abstractmethod
    def _log(self, msg):...
    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'SUCCES: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        raise NotImplementedError(msg)
    
class LogPrintMixin(Log):
    def _log(self,msg):
        m = f'{msg} ({self.__class__.__name__})'
        with open('LogMixin.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(m)
            arquivo.write("\n")


#print(__name__)
if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_sucess('testeee succes')
    l.log_error('testeee error')
'''

# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
'''
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
'''

#Criando Exception
# https://docs.python.org/3/library/exceptions.html
''' 

class MyError(Exception):...

class OutherError(Exception):...

def levantar():
    exception_ = MyError('a', 'b')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except (MyError, Exception) as error_msg:
    print(error_msg.__class__.__name__)
    print(error_msg.args)
    exception_ = OutherError('Lançando outro erro')
    exception_.add_note('mAIS UMA NOTA')
    raise exception_ from error_msg

'''

# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
''' 
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
        
    def __repr__(self):
        #class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Point(novo_x,novo_y)
    
    def __gt__(self,other):
        res_self = self.x + self.y
        res_other = other.x + other.y
        return res_self > res_other
            

p1 = Point(1,2)
p2 = Point(4,5)
p3 = p1 + p2
print(p3)
print(f'p1 é maior do que p?', p2>p1)
#print(repr(p2))
#print(f'{p2!r}')
'''
