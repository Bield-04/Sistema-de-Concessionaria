from classes import Carro, Moto

concessionaria = []

print("Bem-vindo à concessionária!")

while True:
    print("\nQual veículo deseja cadastrar? (Digite 'carro' ou 'moto')")
    escolha = input().lower()
    
    if escolha != 'carro' and escolha != 'moto':
        print("Opção inválida! Tente novamente.")
        continue 
        
    print(f"\n--- Cadastrando {escolha.upper()} ---")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    
    
    if escolha == 'carro':
        novo_veiculo = Carro(marca, modelo, ano)
    else:
        novo_veiculo = Moto(marca, modelo, ano)
        
    concessionaria.append(novo_veiculo)
    
    pergunta = input("\nDeseja adicionar outro veículo? (s/n): ")
    if pergunta.lower() != 's':
        break

print("\n=== Veículos cadastrados na concessionária ===")
for veiculo in concessionaria:
    veiculo.exibir_informacoes()
    
    if isinstance(veiculo, Carro):
        veiculo.abrir_porta()
        
    print("--------------------")
    