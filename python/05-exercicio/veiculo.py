from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def mover(self):
        return "O carro está se movendo."
    
    def frear(self):
        return "O carro está freando."
    
class Bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta está se movendo."
    
    def frear(self):
        return "A bicicleta está freando."
  
  # Criando objetos para teste
carro = Carro()
bicicleta = Bicicleta()

print(carro.mover()) 
print(carro.frear())

print(bicicleta.mover())
print(bicicleta.frear())