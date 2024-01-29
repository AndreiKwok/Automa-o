'''DECORATORS
def decorators(func):
    print('Decoradora')
    def aninhada(*args, **kwargs):
        print('aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

@decorators
@decorators
@decorators
def soma(x,y):
    return x + y
somas = soma(15,5)
print(somas)
'''

#DECORATOR FUNCIONA DE BAIXO PARA CIMA
'''#EXERCICIO BESTA, LISTA
lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_uf = ['BA', 'SP', 'MG', 'RJ']
lista = []
for i in range(len(lista_cidades)):
    tup = (lista_cidades[i], lista_uf[i])
    lista.append(tup)

def zipper(l1,l2):
    range_max = min(len(l1), len(l2))
    return[
        (l1[i], l2[i]) for i in range(range_max)
    ]

#print(zipper(lista_cidades,lista_uf))
print(list(zip(lista_cidades,lista_uf)))'''

l_a= [1, 2, 3, 4, 5, 6, 7]
l_b = [1, 2, 3, 4]
lista_soma = []

for i in range(len(l_b)):
       lista_soma.append(l_a[i] + l_b[i])
    
print(lista_soma)