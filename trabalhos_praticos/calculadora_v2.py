saida =""
def adicao(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        return "Erro: nao pode realizar divisão por zero!"
    else:
        return a / b

def calculadora(a,b,operacao):
    
    op=operacao.lower()

    resultado = 0

    if op == "adicao" or op == "+":
        resultado = adicao(a,b)
    elif op == "subtracao" or op == "-":
        resultado = subtracao(a,b)
    elif op == "multiplicacao" or op == "*":
        resultado = multiplicacao(a,b)
    elif op == "divisao" or op == "/":
        resultado = divisao(a,b)
    else:
        resultado ="Operação inválida!"
    
    return resultado
  
while saida.lower() != "n" :
    try:
          a_input = float(input("Digite o primeiro número: "))
          b_input = float(input("Digite o segundo número: "))
          op_input = input ("Digite a operação (adicao, subtracao, multiplicacao, divisao ou +, -, *, /): ")
          resultado = calculadora(a_input, b_input, op_input)
          print ("Resultado da operação", resultado)

    except ValueError:
          print("Erro: voce digitou um nuemro invalido. Tente novamente")

    except Exception as e:
          print(f"Ocorreu um erro inesperado:{e}")

    print("------------------------")

    saida = input("Deseja Continuar? (S/N)")
    
print("Programa encerrado")
