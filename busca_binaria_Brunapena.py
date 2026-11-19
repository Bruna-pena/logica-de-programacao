
lista = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 81, 89, 94, 99]

numero = int(input("Digite o número que deseja procurar: "))

inicio = 0
fim = len(lista) - 1

comparacoes = 0

while inicio <= fim:

    meio = (inicio + fim) // 2

    comparacoes += 1

    if lista[meio] == numero:
        print(f"Número {numero} encontrado no índice {meio}.")
        break

    elif numero > lista[meio]:
        inicio = meio + 1
      
    else:
        fim = meio - 1

else:
    print(f"Número {numero} não encontrado na lista.")

print(f"Total de comparações realizadas: {comparacoes}")
