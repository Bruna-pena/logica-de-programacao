cadastros = [
   {"nome": "Analyvia", "idade": 16, "curso": "Informática"},
   {"nome": "Eduardo", "idade": 17, "curso": "Administração"}
]

print("--- Sistema de Secretaria Acadêmica ---")


print("\nInsira os dados do novo aluno:")
nome_input = input("Nome do aluno: ")
idade_input = int(input("Idade do aluno: "))
curso_input = input("Curso do aluno: ")


novo_aluno = {
   "nome": nome_input,
   "idade": idade_input,
   "curso": curso_input
}


cadastros.append(novo_aluno)


print("\n--- Lista de Alunos Cadastrados ---")
for aluno in cadastros:
   print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} anos | Curso: {aluno['curso']}")
   print("pronto bryan, quero minha nota")
