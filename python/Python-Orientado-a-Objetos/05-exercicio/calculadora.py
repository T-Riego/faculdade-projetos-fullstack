class Calculadora:
  def somar(self, a, b):
    try:
      return a + b
    except TypeError:
      return "Erro: Os valores devem ser numéricos."

  def subtrair(self, a, b):
    try:
      return a - b
    except TypeError:
      return "Erro: Os valores devem ser numéricos."

  def multiplicar(self, a, b):
    try:
      return a * b
    except TypeError:
      return "Erro: Os valores devem ser numéricos."

  def dividir(self, a, b):
    try:
      return a / b
    except TypeError:
      return "Erro: Os valores devem ser numéricos."
    except ZeroDivisionError:
      return "Erro: Divisão por zero não é permitida."

calculadora = Calculadora()

print(calculadora.somar(10, 5))          # Saída: 15
print(calculadora.subtrair(10, 5))       # Saída: 5
print(calculadora.multiplicar(10, 5))    # Saída: 50
print(calculadora.dividir(10, 0))        # Saída: Erro: Divisão por zero não é permitida.
print(calculadora.dividir(10, 2))        # Saída: 5.0
print(calculadora.somar(10, 'a'))       # Saída: Erro: Os valores devem ser numéricos.