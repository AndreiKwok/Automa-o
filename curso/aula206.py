import json
import os
class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        print(f'{self.nome},{self.idade}')
        
    
class Create_json(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade, cpf)
        lista = []
        j = {
            "Nome": self.nome,
            "Idade": self.idade,
            "CPF": self.cpf
        }
        lista.append(j)
        with open('Pessoa.json','w',encoding='utf-8') as arq:
            json.dump(j, arq, indent=4, ensure_ascii=False)
    
    def __str__(self):
        print("Json criado", self.nome)
        return super().__str__()
    
#p1 = Pessoa()
cj = Create_json('Andrei', '18', '4937777')
    



