💧 Controle de Nível de Água

Sistema simples desenvolvido em Python para simular o monitoramento de um reservatório de água, exibindo alertas coloridos no terminal de acordo com o nível atual.

📌 Objetivo

Este projeto foi desenvolvido como parte de uma atividade do curso técnico em Desenvolvimento de Sistemas, com o objetivo de:

Utilizar estruturas básicas da programação (listas e funções)
Trabalhar com bibliotecas externas
Simular um sistema real de monitoramento
Melhorar a organização e legibilidade do código
⚙️ Funcionalidades
Exibe o nível atual do reservatório
Mostra mensagens com diferentes níveis de alerta
Utiliza cores no terminal para facilitar a visualização:
🔴 Vermelho → Muito baixo (crítico)
🟡 Amarelo → Baixo
🟢 Verde → Médio
🔵 Ciano → Alto
🔷 Azul → Muito alto (alerta)
Restaura automaticamente o estilo padrão do terminal após a execução
🧠 Lógica do Sistema

O sistema foi organizado da seguinte forma:

Uma função (mostrar_nivel) responsável por:
Identificar o nível do reservatório
Exibir a mensagem correspondente
Aplicar a cor adequada
Um valor fixo (nivel_atual) que simula o estado do reservatório
💻 Código Principal
from colorama import Fore, Style, init

# Inicializa o colorama
init()

def mostrar_nivel(nivel):
    if nivel == 1:
        print(Fore.RED + "Nível 1 - Muito baixo (CRÍTICO)")
    
    elif nivel == 2:
        print(Fore.YELLOW + "Nível 2 - Baixo")
    
    elif nivel == 3:
        print(Fore.GREEN + "Nível 3 - Médio")
    
    elif nivel == 4:
        print(Fore.CYAN + "Nível 4 - Alto")
    
    elif nivel == 5:
        print(Fore.BLUE + "Nível 5 - Muito alto (ALERTA)")
    
    else:
        print("Nível inválido")

    # Restaura o estilo padrão
    print(Style.RESET_ALL)


# Simulação do nível atual
nivel_atual = 3

print("=== Situação Atual do Reservatório ===\n")
mostrar_nivel(nivel_atual)
🛠️ Tecnologias Utilizadas
Python 3
Biblioteca Colorama
📦 Como Executar o Projeto
1. Clone o repositório
git clone https://github.com/seu-usuario/controle-nivel-agua.git
2. Acesse a pasta
cd controle-nivel-agua
3. Instale a biblioteca necessária
pip install colorama
4. Execute o programa
python main.py
📈 Possíveis Melhorias
Permitir entrada de dados pelo usuário
Monitoramento em tempo real (loop contínuo)
Armazenamento de histórico dos níveis
Interface gráfica (GUI)
Integração com sensores (IoT)
🎓 Contexto Acadêmico

Atividade prática voltada para o desenvolvimento de:

Raciocínio lógico
Organização de código
Uso de funções e bibliotecas
Simulação de sistemas reais
👨‍💻 Autor

Paulo
Estudante do curso técnico em Desenvolvimento de Sistemas

📄 Licença

Este projeto é de uso educacional.