nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print(type(nota1))
print(type(nota2))

media = (nota1 + nota2) / 2
print(f"A média das notas é: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")