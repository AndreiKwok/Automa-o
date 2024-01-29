#############################################################################################################
'''
INTEGRANTES: 
Andrei Fernandes Kwok // RA: 2301306
Eduardo Paro Costa // RA: 2300613
Kaique Batista Tamos // RA: 2300281
'''
#############################################################################################################
import json
import os
import time

def inserir():
     if os.path.exists('clientes.json'):
         with open('clientes.json', 'r', encoding='utf-8') as arq:
             dados = json.load(arq)
     else:
         dados = []

     id = int(input('Digite o id do cliente: '))
     nome = str(input('Digite o nome do cliente: ')).capitalize()
     cpf = str(input('Digite o cpf do cliente: '))
     end = str(input('Digite o endereço do cliente(Rua e Nº):'))

     infos = {
         "id": id,
         "nome": nome,
         "cpf": cpf,
         "endereco": end
     }
     cad = False
     for item in dados:
         if item['id'] == id:
             print('Cliente já cadastrado.')
             cad = True
             break

     if cad == False:
         dados.append(infos)
         with open('clientes.json', 'w', encoding='utf-8') as arq:
             json.dump(dados, arq, indent=4, ensure_ascii=False)
         print('Cliente cadastrado.\n')


def excluir():
     if os.path.exists('clientes.json'):
         with open('clientes.json', 'r', encoding='utf-8') as arq:
             dados = json.load(arq)

             id = int(input('Digite o id que deseja excluir: '))
             cad = False
             for item in dados:
                 if item['id'] == id:
                     dados.remove(item)
                     print('Cliente excluido.\n')
                     cad = True
                     break

             if cad == True:
                 with open('clientes.json', 'w', encoding='utf-8') as arq:
                     json.dump(dados, arq, indent=4, ensure_ascii=False)
             else:
                 print('Não há cliente cadastrado com este id.\n')
     else:
         print('Não há cliente cadastrado com este id.\n')

def alterar():
    if os.path.exists('clientes.json'):
         with open('clientes.json', 'r', encoding='utf-8') as arq:
             dados = json.load(arq)
             cad = False

             id = int(input('Digite o id do cliente que deseja alterar:'))
             for item in dados:
                 if item['id'] == id:
                     n_atual = input('Digite o Nome do cliente: ')
                     cpf_atual = input('Digite o cpf do cliente: ')
                     end_atual = input('Digite o endereço do cliente: ')
                     item['nome'] = n_atual
                     item['cpf'] = cpf_atual
                     item['endereco'] = end_atual
                     print(f'Informações do cliente com id {id} alteradas.\n')
                     cad = True
                     break

             if cad == True:
                 with open('clientes.json', 'w', encoding='utf-8') as arq:
                     json.dump(dados, arq, indent=4, ensure_ascii=False)
             else:
                 print('Não há cliente cadastrado com este id.\n')
    else:
        print('Não há clientes cadastrados.')


def listar():
    cont = False
    if os.path.exists('clientes.json'):
         with open('clientes.json', 'r', encoding='utf-8') as arq:
             dados = json.load(arq)
             for i in dados:
                print(i)
                cont = True
    if cont == False:
        print('Não há cliente cadastrado.\n')
        
while True:
    print('DIGITE A SUA OPÇÃO:\n'
          f'[ 1 ] INSERIR\n'
          f'[ 2 ] EXCLUIR\n'
          f'[ 3 ] ALTERAR\n'
          f'[ 4 ] LISTAR\n'
          f'[ 5 ] SAIR')
    time.sleep(0.5)
    opcao = int(input())
    if opcao == 1:
        inserir()
    elif opcao == 2:
        excluir()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        listar()
    else: break
