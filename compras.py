produto = "Feijão"
preco = 7.50
quantidade = 3


total = preco * quantidade

if quantidade >= 2:
    desconto = total * 0.10 # 10% de desconto
else:
    desconto = 0

total_com_desconto = total - desconto
print(f"Produto: {produto}")
print(f"Preço unitário: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total com desconto: R$ {total_com_desconto:.2f}")