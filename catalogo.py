catalogo = [
  {"produto": "Mouse Pad", "preco": 35.0, "em_estoque": True},
  {"produto": "Headset", "preco": 180.0, "em_estoque": False}
]

for item in catalogo:
  print(f"Item: {item['produto'] - R$ {item['preco']:.2f}")
