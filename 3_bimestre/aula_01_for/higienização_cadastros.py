#exercício 1: Padronização de nome
nome = "joão pedro da silva"
email = "JOAO.SILVA@escola.com"

nome_higienizado = nome.strip().upper()
email_higienizado = email.strip().lower()

print("Nome higienizado: ", nome_higienizado)
print("Email higienizado: ", email_higienizado)

#ecercíco 2: Limpeza de documentos
cpf = "123.456.789-00"
telefone = "(11) 99999-8888"

cpf_limpo = cpf.strip().replace(".","").replace("-","").replace(" ","")
telefone_limpo = telefone.strip().replace("(","").replace(")","").replace("-","").replace(" ","")
print("CPF limpo: " cpf_limpo)
print("Telefone limpo: " telefone_limpo)

#exercício 3: Padronização de SKU
codigo = "prod-1024-br-sp"
codigo_formatado = codigo.strip().upper().replace("-","_")
print("Código formatado: ", codigo_formatado)
