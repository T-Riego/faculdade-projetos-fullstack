import threading
import urllib.request
import time

start = time.time()
urls = ["http://google.com", "http://yahoo.com", "http://bing.com", "http://ask.com"]

def chama_url(url):
    """Função que faz a requisição HTTP e imprime o tempo de resposta."""
    try:
        # A sintaxe de requisição em Python 3
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        
        # Lê o conteúdo da página
        the_page = response.read()
        
        # Imprime o resultado e o tempo gasto
        print("%s carregado em %.4f segundos" % (url, (time.time() - start)))
        
        # Descomente a linha abaixo se quiser ver o conteúdo de todas as páginas
        #print(the_page) 
        
    except Exception as e:
        # Tratamento de erro básico
        print(f"Erro ao carregar {url}: {e}")


# 1. Criação das Threads usando List Comprehension
threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

# 2. Inicia a execução de todas as threads
for thread in threads:
    thread.start()

# 3. Espera que todas as threads terminem (o comando join() faz o 'await')
for thread in threads:
    thread.join()

print("--------------------------------------------------")
print("Tempo total: %.4f segundos" % (time.time() - start))