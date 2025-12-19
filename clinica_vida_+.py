# ======================================================
# SISTEMA CLÍNICA VIDA+
# Projeto Integrado – ADS
# ======================================================

# ------------------------------
# DADOS
# ------------------------------
pacientes = []
fila_atendimento = []

# ------------------------------
# FUNÇÕES DO SISTEMA
# ------------------------------

def cadastrar_paciente():
    print("\n=== CADASTRO DE PACIENTE ===")
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")

        pacientes.append({
            "nome": nome,
            "idade": idade,
            "telefone": telefone
        })

        print("Paciente cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: idade inválida.\n")


def listar_pacientes():
    print("\n=== LISTA DE PACIENTES ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
    print()


def buscar_paciente():
    print("\n=== BUSCAR PACIENTE ===")
    nome = input("Digite o nome do paciente: ").lower()

    encontrados = [p for p in pacientes if p["nome"].lower() == nome]

    if encontrados:
        for p in encontrados:
            print(p)
    else:
        print("Paciente não encontrado.\n")


def estatisticas_pacientes():
    print("\n=== ESTATÍSTICAS ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    total = len(pacientes)
    media = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.2f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']})")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']})\n")


# ------------------------------
# CONTROLE DE ATENDIMENTO (LÓGICA)
# ------------------------------

def consulta_normal(A, B, C, D):
    return (A and B and C) or (B and C and D)


def emergencia(B, C, D):
    return C and (B or D)


def verificar_atendimento():
    print("\n=== CONTROLE DE ATENDIMENTO ===")
    A = input("Tem agendamento? (s/n): ").lower() == "s"
    B = input("Documentos OK? (s/n): ").lower() == "s"
    C = input("Médico disponível? (s/n): ").lower() == "s"
    D = input("Pagamentos em dia? (s/n): ").lower() == "s"

    if consulta_normal(A, B, C, D):
        print("✔ Atendimento autorizado (Consulta Normal)\n")
    elif emergencia(B, C, D):
        print("⚠ Atendimento autorizado (Emergência)\n")
    else:
        print("❌ Atendimento NÃO autorizado\n")


# ------------------------------
# FILA DE ATENDIMENTO
# ------------------------------

def adicionar_fila():
    print("\n=== ADICIONAR À FILA ===")
    nome = input("Nome do paciente: ")
    cpf = input("CPF: ")
    fila_atendimento.append({"nome": nome, "cpf": cpf})
    print("Paciente adicionado à fila.\n")


def atender_paciente():
    print("\n=== ATENDIMENTO ===")
    if not fila_atendimento:
        print("Fila vazia.\n")
        return

    atendido = fila_atendimento.pop(0)
    print("Paciente atendido:")
    print(atendido)
    print()


def mostrar_fila():
    print("\n=== FILA DE ATENDIMENTO ===")
    if not fila_atendimento:
        print("Fila vazia.\n")
        return

    for p in fila_atendimento:
        print(p)
    print()


# ------------------------------
# MENU PRINCIPAL
# ------------------------------

def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Buscar paciente")
        print("4. Estatísticas dos pacientes")
        print("5. Verificar atendimento (Lógica)")
        print("6. Adicionar paciente à fila")
        print("7. Atender próximo da fila")
        print("8. Mostrar fila")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            listar_pacientes()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            estatisticas_pacientes()
        elif opcao == "5":
            verificar_atendimento()
        elif opcao == "6":
            adicionar_fila()
        elif opcao == "7":
            atender_paciente()
        elif opcao == "8":
            mostrar_fila()
        elif opcao == "9":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!\n")


# ------------------------------
# EXECUÇÃO
# ------------------------------
menu()
