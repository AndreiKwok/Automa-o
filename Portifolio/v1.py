from datetime import datetime, date, timedelta, time
from time import sleep
import sys
import os
import json
from easygui import msgbox
#VLIDAR OQ ESTA SENDO CRIADO NO JSON E SE INSERIU AS DEMAIS INFOS




#Intenção é add uma "folha de ponto para os funcionarios"
#Cadastramento da Empresa
class Empresa:
    def __init__(self, nome, cnpj, dono):
        self.nome = nome
        self.cnpj = cnpj
        self.dono = dono

    #def cadastro(self):
     #   return f'{self.nome},{self.cnpj},{self.endereco}'

#Cadastramento de Funcionarios
class Pessoas:
    def __init__(self, nome, idade, cpf, endereco, tel_cont):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        self.endereco = endereco
        self.tel_cont = tel_cont
        
class Funcionario(Pessoas):
    def __init__(self, nome, idade, cpf, endereco, tel_cont, cargo, salario, id): 
        super().__init__(nome, idade, cpf, endereco, tel_cont)
        self.cargo = cargo
        self.salario = salario
        self.id = id
    
    def cadastro(self):
        if os.path.exists('Cadastro_Func.json'):
            with open('Cadastro_Func.json', 'r', encoding='utf-8') as arq:
                dados = json.load(arq)
        else:
            dados = []
            msgbox('aqui')
        self.funcionario = {
            "id": self.id,
            "nome": self.nome,
            "tel": self.tel_cont,
            "cargo": self.cargo
        }
        print(self.funcionario)

        cad = False
        for item in dados:
            if item["id"] == self.id:
                cad = True
                return 'Funcionario já cadastrado.', sys.exit()
                
            
        if not cad:
            dados.append(self.funcionario)
            msgbox(dados)
            with open('Cadastro_Func.json', 'a+', encoding='utf-8') as arq:
                json.dump(dados, ensure_ascii=False, indent=4)
                return 'Funcionario cadastrado com sucesso.'


    
    def __str__(self):
        self.funcionario = self.id
        return self.funcionario

# Cadastro do Departamento
class Departamento(Empresa):
    def __init__(self, nome, cnpj, dono,departamento):
        super().__init__(nome, cnpj, dono)
        self.depto = departamento

    def cadastro(self):
        return f"Departamento {self.depto} cadastrado!"

class Ponto(Funcionario):
    def __init__(self, nome, idade, cpf, endereco, tel_cont, cargo, salario,id, mood):
        super().__init__(nome, idade, cpf, endereco, tel_cont, cargo, salario, id)
        self.mood = mood
        self.date = datetime.today().strftime('%d/%m/20%y')

    
    def validacao_funcionario(self, funcionario_id):
        super().__str__()
        if self.funcionario == funcionario_id:
            return True
        else: return False

    def bater_ponto(self,valid,mood):
        if valid == True and str(mood).lower() == 'entrada':
            self.time = datetime.now().strftime('%H:%M:%S')
            return f'Horário de entrada: {self.date} às {self.time}'

        if valid == True and str(mood).lower() == 'saida':
            self.time = datetime.now().strftime('%H:%M:%S')
            return f'Horário de saída: {self.date} às {self.time}'
        
        if valid == True and str(mood).lower() == 'almoco':
            self.time = datetime.now()
            #self.time_f = datetime(self.time)
            self.time_back =  self.time + timedelta(hours=1)
            print(f'Você tem 1hr para retornar. Se atente ao horario de volta às {self.time_back.strftime("%H:%M:%S")}')
            return f'Horário de saída: {self.date} às {self.time.strftime("%H:%M:%S")}'
        
        if valid == True and str(mood).lower() == 'volta_almoco':
            self.time = datetime.now()
            #self.time_f = datetime(self.time)
            return f'Horário de volta: {self.date} às {self.time.strftime("%H:%M:%S")}'

        
            
#empresa = Empresa("FK'Company", "500.700.222.5555", "Rua do tio zeze, 291")
#print(empresa.cadastro())
f = Funcionario('Andrei', 18, '493.775.348-79', 'Rua Pereba, 291', '(11)98047-6869', 'chefe', '30.000', 1)
print(f.cadastro())
f = 1
#print(p.validacao_funcionario(f))
#print(p.bater_ponto(f, 'volta_almoco'))
#d = Departamento("FK'Company","500.700.222.5555", "Rua do tio zeze, 291", 'Desenvolvimento')
#print(d.cadastro())
''' 
while True:
    print("FK'Company\n"
        f'Digite a sua opção desejada.\n'
        f'[ 1 ] CAD Departamento\n'
        f'[ 2 ] CAD Funcionário\n' 
        f'[ 3 ] FOLHA DE PONTO\n'   
        f'[ 4 ] SAIR'      
        )
    sleep(1)
    
    op = int(input())
    if op == 1:
        name = input('Digite o nome do departamento: ')
        cnpj = input('Digite o CNPJ do depto.:')
        end = input('Digite o endereço do depto.:')
        depto = input('Digite o depto.:')
        d = Departamento(name, cnpj, end, depto)
        print(f"{d.cadastro()}\n")

    if op == 3:
        sys.exit()
'''
    

'''print("FK'Company\n"
        f'Digite a sua opção desejada.\n'
        f'[ 1 ] ENTRADA\n'
        f'[ 2 ] SAIDA\n'
        f'[ 3 ] ALMOÇO\n'
        f'[ 4 ] VOLTA DO ALMOÇO'            
        )
    op = int(input())'''