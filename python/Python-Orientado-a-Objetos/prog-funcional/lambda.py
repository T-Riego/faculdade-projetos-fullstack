#Exercicio 1
veiculos = ['aviao', 'carro', 'barco', 'moto']

f_maiuculas = lambda x: str.upper(x)
#a função str upper serve para converter em maiúsculos com a função lambda

nomes_maiusculas = list(map(f_maiuculas, veiculos))
#map utilizado para aplicar a função f_maiuculas em cada elemento da lista veiculos

print(f'nomes maiusculas: {nomes_maiusculas}')

#Exercicio 2

lista = [0,1,1,2,3,5,8,13,21,34,55]

f_pares = lambda x: x % 2 == 0
#função lambda para verificar se o número é par

print(f'teste função pares: {f_pares(5)}')

numeros_pares = list(filter(f_pares, lista))
#filter , aplica um filtro e retorna apenas o que estiver indicado para ele fazer

print(f'numeros pares: {numeros_pares}')

#Exercicio 3 
#implementar uma solução que utilize a função lambda para arredondar uma lista de números
lista_numeros = [9.56783, 4.3567, 8.1234, 6.9874, 3.4567]
lista_precisao = [2,2,3,3,1]

arredondados = lambda x,y: round(x,y)
resultado = list(map(arredondados, lista_numeros, lista_precisao))
print(resultado)

#Exercicio 4
#impmentar uma solução que utilize a função lambda para somar todos os elementos da lista
from functools import reduce

f_soma = lambda x,y: x + y

numero= [1,2,3,4,5,6,7,8,9,10]

soma_total = reduce(f_soma, numero)
print(f'soma total: {soma_total}')