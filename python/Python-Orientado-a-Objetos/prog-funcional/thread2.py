# inicie a execução de uma Thread
# Coloque a thread para esperar 2 segundos
# informe o inicio e o final da execução da Thread

from time import sleep
from threading import Thread

def tarefa(tempo_espera,mensagem):
    print(f'Iniciando a tarefa: {mensagem}')
    sleep(tempo_espera)
    print(f'Tarefa finalizada: {mensagem}')
  
#instanciando a Thread , o target se refere a função que será executada pela Thread,
#o arg são os parametros dessa função
thread = Thread(target=tarefa, args=(2,'Thread em execução'))
thread.start()
print ('\nAguardando o término da Thread\n')
thread.join()
#join serve para esperar o resultado
print('\nThread finalizada\n')