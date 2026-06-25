import tkinter as tk
from classes import Carro, Moto

janela = tk.Tk()
janela.title("Sistema da Concessionária")
janela.geometry("400x550") # Aumentei um pouco a altura para caber a lista

concessionaria = []

# --- FUNÇÕES ---

def cadastrar_carro():
    marca = campo_marca.get()
    modelo = campo_modelo.get()
    ano = campo_ano.get()
    
    if marca and modelo and ano: # Garante que não está vazio
        novo_carro = Carro(marca, modelo, ano)
        concessionaria.append(novo_carro)
        label_aviso.config(text=f"Carro {modelo} cadastrado!", fg="white")
        limpar_campos()
    else:
        label_aviso.config(text="Preencha todos os campos!", fg="red")

def cadastrar_moto():
    marca = campo_marca.get()
    modelo = campo_modelo.get()
    ano = campo_ano.get()
    
    if marca and modelo and ano:
        novo_moto = Moto(marca, modelo, ano)
        concessionaria.append(novo_moto)
        label_aviso.config(text=f"Moto {modelo} cadastrada!", fg="white")
        limpar_campos()
    else:
        label_aviso.config(text="Preencha todos os campos!", fg="red")

def limpar_campos():
    campo_marca.delete(0, tk.END)
    campo_modelo.delete(0, tk.END)
    campo_ano.delete(0, tk.END)

# NOVA FUNÇÃO PARA LISTAR
def listar_veiculos():
    # Habilita a caixa de texto para edição
    campo_lista.config(state=tk.NORMAL)
    
    # Limpa o que estava escrito antes para não duplicar
    campo_lista.delete("1.0", tk.END)
    
    if not concessionaria:
        campo_lista.insert(tk.END, "Nenhum veículo cadastrado ainda.\n")
    else:
        # Loop que passa por cada objeto da lista
        for veiculo in concessionaria:
            # O Python usa o __str__ que criamos na classe automaticamente aqui
            campo_lista.insert(tk.END, f"{veiculo}\n")
            
    # Desabilita a caixa de texto para o usuário não conseguir digitar nela
    campo_lista.config(state=tk.DISABLED)


# --- ELEMENTOS DA TELA (INTERFACE) ---

label_marca = tk.Label(janela, text="Marca do Veículo:")
label_marca.pack(pady=5)
campo_marca = tk.Entry(janela)
campo_marca.pack()

label_modelo = tk.Label(janela, text="Modelo do Veículo:")
label_modelo.pack(pady=5)
campo_modelo = tk.Entry(janela)
campo_modelo.pack()

label_ano = tk.Label(janela, text="Ano do Veículo:")
label_ano.pack(pady=5)
campo_ano = tk.Entry(janela)
campo_ano.pack()

# Botões de cadastro
carro_button = tk.Button(janela, text="Cadastrar como Carro", fg="green", command=cadastrar_carro)
carro_button.pack(pady=5)

moto_button = tk.Button(janela, text="Cadastrar como Moto", fg="blue", command=cadastrar_moto)
moto_button.pack(pady=5)

label_aviso = tk.Label(janela, text="")
label_aviso.pack(pady=5)

# NOVO BOTÃO DE LISTAR
botao_listar = tk.Button(janela, text="🔄 Atualizar/Listar Veículos", command=listar_veiculos)
botao_listar.pack(pady=10)

# NOVA CAIXA DE TEXTO PARA MOSTRAR A LISTA
# width=40 (largura em caracteres), height=8 (linhas de altura)
campo_lista = tk.Text(janela, width=40, height=8, state=tk.DISABLED)
campo_lista.pack(pady=5)

janela.mainloop()
