class Veiculo: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

class Carro(Veiculo):
    def abrir_porta(self):
        print(f"Porta do {self.modelo} aberta.")
        
    def __str__(self):
        return f"🚗 Carro: {self.marca} {self.modelo} ({self.ano})"

class Moto(Veiculo):
    def empinar(self):
        print(f"A moto {self.modelo} está empinando!")
            
    def __str__(self):
        return f"🏍️ Moto: {self.marca} {self.modelo} ({self.ano})"
