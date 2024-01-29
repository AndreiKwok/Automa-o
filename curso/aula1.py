#Serve para armazenar as libs e subir no github, ao inves de mandar a venv. comando: "pip freeze > requirements.txt"
#Porém tomar cuidado pois serve para todos os projetos, se torna global, caso não tenha a venv
#Se atentar para tomar cuidado e manter nos projetos certos
#easygui==0.98.3
import json

with open('C:\\Desenvolvimento\\Projetos\\VsCodeProjects\\clientes.json', 'r', encoding='utf-8') as arq:
    dados = json.load(arq)
    for item in dados:
        print(item)