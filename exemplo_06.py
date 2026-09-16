leituras = []
quantidade = int(input("Quantas Leituras?: "))
for i in range (quantidade):
    valor = float(input(f"Leitura {i + 1}: "))
    leituras.append(valor)
    print(f"Leitura atualizada ! {valor}")
for i in leituras:
    print(i)