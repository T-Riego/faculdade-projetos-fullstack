veiculos = ['aviao', 'carro', 'barco', 'moto']

f_maiuculas = lambda x: str.upper(x)
#a função str upper serve para converter em maiúsculos com a função lambda

nomes_maiusculas = list(map(f_maiuculas, veiculos))
#map utilizado para aplicar a função f_maiuculas em cada elemento da lista veiculos

print(f'nomes maiusculas: {nomes_maiusculas}')

lista = [0,1,1,2,3,5,8,13,21,34,55]