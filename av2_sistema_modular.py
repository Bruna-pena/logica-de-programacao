# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno:
# Data: 18/09/2026
# Link do Repositório:
# ==============================================================================

# Lista inicial de dados brutos
# Formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    Remove espaços extras das pontas e converte o texto para MAIÚSCULAS.
    """
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    
    FUNÇÃO 2:
    Remove espaços das pontas e utiliza fatiamento [x:y]
    para extrair os 2 primeiros dígitos do dado.
    
    dado_limpo = dado.strip()
    codigo = dado_limpo[0:2]
    return codigo


def processar_e_exibir_cadastros(lista_dados):
    
    FUNÇÃO 3:
    Percorre a lista de cadastros, separa os dados, formata nome
    e cargo, extrai o DDD e exibe os resultados.
    """
    total_processado = 0

    for dado in lista_dados:
        partes = dado.strip().split(";")

        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])
        ddd = extrair_codigo_ou_ddd(partes[2])

        print(f"Nome: {nome}")
        print(f"Cargo/Setor: {cargo}")
        print(f"DDD/Código: {ddd}")
        print("-" * 50)

        total_processado += 1

    return total_processado


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    # Chamada da Função 3 passando a lista de dados.
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Exibe a quantidade total de registros processados.
    print(f"Total de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


# Execução do programa
if __name__ == "__main__":
    main()
