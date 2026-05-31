# Importando biblioteca
from colorama import Fore, Style, init

# Inicializando colorama
init(autoreset=True)

# Lista de níveis do reservatório
niveis = [1, 2, 3, 4, 5]

# Função para exibir o status com cores
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

# Restaurar estilo após exibir
print(Style.RESET_ALL)

# 🔹 SIMULAÇÃO DE UM NÍVEL ATUAL
nivel_atual = 2  # você pode mudar esse valor

print("=== Situação Atual do Reservatório ===\n")

mostrar_nivel(nivel_atual)