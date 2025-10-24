#Implementar uma solução por Thread que faça:
#Inicie a execução de duas threads,
# coloque a primeira a segunda para esperar respectivamente 3 2 segundos 
# e informe a ordem de execução das threads

from time import sleep
from threading import Thread

def tarefa(tempo_espera,nome_tarefa):
    print(f'Iniciando a tarefa: {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Tarefa finalizada: {nome_tarefa}')

thread1 = Thread(target=tarefa, args=(3,'A'))
thread2 = Thread(target=tarefa, args=(2,'B'))
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("\nTodas as threads finalizadas\n")



