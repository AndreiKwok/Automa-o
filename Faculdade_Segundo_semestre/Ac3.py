import easygui
class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def __str__(self):
        return(f'Nome do poder: {self.__nome}\n'
               f'Categoria do poder: {self.__categoria}')

    def get_nome(self):
        return(self.__nome)
    
    def get_categoria(self):
        return(self.__categoria)
    
class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes_nome = []
        self.__poderes_categoria = []

    def __str__(self):
        return(self.__nome)

    def adicionar_super_poder(self, superpoder):
        self.superpoder = superpoder
        if superpoder.get_nome() not in self.__poderes_nome:
            self.__poderes_nome.append(superpoder.get_nome())
            self.__poderes_categoria.append(superpoder.get_categoria())
            
        else:
            pass
            print('Super poder já inserido')

    def get_poder_total(self):
        self.poder_total = 0
        for i in self.__poderes_categoria:  
            self.poder_total += i 
        return self.poder_total

class SuperHeroi(Personagem):
    def get_poder_total(self):
       super().get_poder_total()
       poder_super_heroi = (self.poder_total * 0.05) + self.poder_total
       self.poder_total = float(poder_super_heroi)
       return(self.poder_total)
    
    def __str__(self):
        return super().__str__(),  self.poder_total
                
class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao

    def __str__(self):
        return super().__str__(),vilao.get_poder_total()

class Confronto:
    def lutar(self, superheroi, vilao):
        superheroi = str(superheroi).strip('()').split()
        poder_superheroi = float(superheroi[1])
        vilao = str(vilao).strip('()').split()
        poder_vilao = float(vilao[1])
        
        if poder_superheroi > poder_vilao:
           print('entrou no if')
           return(f'O vencedor da batalha é {poder_superheroi} !!!')
            
        elif  poder_vilao> poder_superheroi:
            return(f'O vencedor da batalha é {poder_vilao} !!!')
        else:
            print('')

confronto = Confronto()
Lista_personagem = []
Lista_poder = []

print('INSIRIR SUPER-HERÓI')
try:
    nome_heroi = input('Digite o nome do Super-heroi: ').capitalize()
    nome_real = input('Digite o nome real do heroi: ').capitalize()
    superheroi = SuperHeroi(nome_heroi, nome_real)
except Exception as error_msg:
    print(f'ERROR: {error_msg}')

try:
    while True:
        options_power = input('Deseja inserir poderes ao Heroi?(S/N): ').upper()
        if options_power == 'S':
            nome_poder = input('Digite o nome do poder: ')
            categoria = float(input('Digite a categoria do poder: '))
            superpoder = SuperPoder(nome_poder, categoria)
            superheroi.adicionar_super_poder(superpoder)
        else: 
            Lista_poder.append(superheroi.get_poder_total())
            superheroi.get_poder_total()
            a = superheroi.__str__()
            break

except Exception as error_msg:
    print(f'ERROR: {error_msg}')

print(f'heroi again {a}')
try:
    print('INSIRA O VILÃO')
    nome_vilao = input('Digite o nome do Vilão: ').capitalize()
    nome_real = input('Digite o nome real do vilão: ').capitalize()
    tempo_prisao = float(input('Digite o tempo de prisão do vilão: '))
    vilao = Vilao(nome_vilao, nome_real, tempo_prisao)
except Exception as error_msg:
    print(f'ERROR: {error_msg}')
try:
    while True:
        options_power = input('Deseja inserir poderes ao Vilão?(S/N): ').upper()
        if options_power == 'S':
            nome_poder = input('Digite o nome do poder: ')
            categoria = float(input('Digite a categoria do poder: '))
            superpoder_vilao = SuperPoder(nome_poder, categoria)
            Lista_personagem.append(vilao)
            vilao.adicionar_super_poder(superpoder_vilao)
        else:
            Lista_poder.append(vilao.get_poder_total())
            vilao.get_poder_total()
            b = vilao.__str__()

            break

except Exception as error_msg:  
    print(f'ERROR: {error_msg}')

try:
    confronto1 = confronto.lutar(a, b)
    print(confronto1)
except Exception as error_msg:
    print(f'ERROR: {error_msg}')
