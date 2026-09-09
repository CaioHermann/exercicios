consumo = float(input("Insira o consumo: "))
custo_base = consumo * 0.5

resposta_verao = input("O consumo foi no verão? (1 - Sim / 2 - Não): ").lower().strip()

verao = not (resposta_verao == "2" or resposta_verao == "não")

if consumo > 300 and verao:
    taxa_bandeira = 15.00
    print("Bandeira Vermelha (Consumo crítico no verão!)")
elif consumo > 200 or (consumo > 150 and verao):
    taxa_bandeira = 7.50
    print("Bandeira Amarela (Consumo elevado no verão!)")
else:
    taxa_bandeira = 0
    print("Sem bandeira (Consumo normal)")

valor_total = custo_base + taxa_bandeira

print(f"Custo base: R$ {custo_base:.2f}")
print(f"Taxa de bandeira: R$ {taxa_bandeira:.2f}")
print(f"Custo total: R$ {valor_total:.2f}")