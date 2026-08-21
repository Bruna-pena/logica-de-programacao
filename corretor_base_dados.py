brutos = [
  " MARIA DA SILVA ",
  "joao.souza@EMAIL.com",
  " RUA DAS FLORES, No 123 ",
  " 000.111.222-33 ",
  "CARLOS.ROCHA@ESCOLA.ORG ",
  " AV. CENTRAL, No 450 "
]

# --- LÓGICA DE PROCESSAMENTO EM LOTE ---
for item in brutos:
  # 1. Remove espaços extras nas extremidades
  texto = item.strip()

# 2. Se for e-mail (contém '@'), converte inteiramente para minúsculas 
if "@" in texto:
  texto = texto.lower()
else:
  # 3. Corrige abreviação "No" para "Número"
  texto = texto.replace("No", "Número")
  # 4. Remove pontuações de CPF e endereços (pontos e hífens)
  texto = texto.replace(".", "").replace("-", "")
  # 5. Adiciona o dado sanitizado na lista final
  dados_limpos.append(texto)
  # --- EXIBIÇÃO FORMATADA DOS RESULTADOS ---
  print("  BASE DE DADOS TRATADA E SANITIZADA  ") 
for i, elemento in enumerate(dados_limpos, start=1):
  print(f"{i:02d}; {elemento}")
