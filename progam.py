nota1 = int(input("Digite a primeira nota "))
nota2 = int(input("Digite a segunda nota "))
nota3 = int(input("Digite a terceira nota "))

med = (nota1 * 1 + nota2 * 1 + nota3 * 2) / (1 + 1 + 2)

print(f"Média é: ", med)

if med > 6:
  print("Aprovado")

elif med>5:
  print("Recuperação")
else:
  print("Reprovado")