# inicie 2 threads
# a primeira vai calcular o cubo de um numero
# a segunda vai clcular o quadrado de um numero
# coloque a primeira e a segunda para esperar 2 e 3 segundos respectivamente
# informe a ordem de exercução das threads
# primeiro importar as bibliotecas necessárias, depois criar as threads que serao 
# necessárias para realizar as tarefas. com target e args. depois implementar as def

from time import sleep
from threading import Thread

def calcular_cubo(numero, tempo_espera):
    print(f'Calculando o cubo de {numero}')
    sleep(tempo_espera)
    resultado = numero ** 3
    print(f'O cubo de {numero} é {resultado}')

def calcular_quadrado(numero, tempo_espera):
    print(f'Calculando o quadrado de {numero}')
    sleep(tempo_espera)
    resultado = numero ** 2
    print(f'O quadrado de {numero} é {resultado}')

thread_cubo = Thread(target=calcular_cubo, args=(5,3))
thread_quadrado = Thread(target=calcular_quadrado, args=(4,2))

thread_cubo.start()
thread_quadrado.start() 
thread_cubo.join()
thread_quadrado.join()

print( "\nTodas as threads finalizadas\n")