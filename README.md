# 🚗 Sistema de Gerenciamento de Concessionária

Um Sistema de Concessionaria feito em Python

Um sistema desktop simples e eficiente para cadastro e listagem de veículos (Carros e Motos), desenvolvido em Python utilizando a biblioteca gráfica **Tkinter** e conceitos avançados de **Orientação a Objetos (POO)**.

---

## 🚀 Funcionalidades

* **Cadastro por Categoria:** Permite cadastrar veículos diferenciando entre Carros e Motos.
* **Validação de Campos:** O sistema impede cadastros com campos vazios e emite alertas visuais.
* **Polimorfismo e Herança:** Uso de uma classe mãe (`Veiculo`) para reaproveitamento de código.
* **Listagem em Tempo Real:** Uma área de texto dinâmica que exibe todos os veículos cadastrados no sistema com formatação personalizada.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface Gráfica:** Tkinter (Nativo do Python)
* **Paradigma:** Programação Orientada a Objetos (POO)

---

## 📁 Estrutura do Projeto

* `classes.py`: Contém a lógica de negócios, incluindo a classe mãe `Veiculo` e as classes filhas `Carro` e `Moto` com seus respectivos métodos e sobrecarga do método `__str__`.
* `app.py`: Arquivo principal contendo a interface gráfica, gerenciamento de estados dos componentes e funções de clique dos botões.

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone este repositório ou baixe os arquivos na mesma pasta.
3. Se estiver no Linux (como Ubuntu/Kubuntu) e o Tkinter não estiver instalado, execute:
   ```bash
   sudo apt install python3-tk
