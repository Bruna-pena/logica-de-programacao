valor = 1200

print("=" * 36)
print(f"TABELA DE PARCELAMENTO - COMPRA R$ {valor:.2f}")
print("=" * 36)

for parcelas in range(1, 11):
    valor_parcela = valor / parcelas
    print(f"{parcelas}x de R$ {valor_parcela:.2f}")