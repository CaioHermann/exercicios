leituras = []

quantidade = int(input("Insira a quantidade de leituras desejadas: "))
for i in range(quantidade):
    valor = float(input(f"Digite o valor da leitura {i + 1}: "))
    leituras.append(valor)
    print(f"Lista atualizada: {leituras}\n")

print(f"Maior leitura: {max(leituras)}")
print(f"Menor leitura: {min(leituras)}")
print(F"Soma das leituras: {sum(leituras)}")
