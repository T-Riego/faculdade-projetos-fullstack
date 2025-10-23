from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def frear(self):
        pass
    
    @abstractmethod
    def ligar(self):
        pass
    
    def voar(self):
        return "O veículo está voando."


class Carro(Veiculo):
    def mover(self):
        return "O carro está se movendo."
    
    def frear(self):
        return "O carro está freando."
    
    def ligar(self):
        return "O carro está ligando."

class Bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta está se movendo."
    
    def frear(self):
        return "A bicicleta está freando."
    
    def ligar(self):
        return "A bicicleta não possui ignição."
  
class Aviao(Veiculo):
    def mover(self):
        return "O avião está voando."
    
    def frear(self):
        return "O avião está aterrissando."

    def ligar(self):
        return "O avião está ligando."

  # Criando objetos para teste
carro = Carro()
bicicleta = Bicicleta()
aviao = Aviao()

print(carro.mover()) 
print(carro.frear())

print(bicicleta.mover())
print(bicicleta.frear())

print(aviao.mover())
print(aviao.ligar())