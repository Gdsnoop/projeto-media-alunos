#Solicita ao usuario notas as 3 notas para a média
nota1 = int(input("Digite a primeira nota "))
nota2 = int(input("Digite a segunda nota "))
nota3 = int(input("Digite a terceira nota "))

# Cálculo da média ponderada:
# A primeira e a segunda nota têm peso 1, e a terceira nota tem peso 2.
med = (nota1 * 1 + nota2 * 1 + nota3 * 2) / (1 + 1 + 2)

#Exibe a média da nota
print(f"Média é: ", med)

# Condicional que verifica a situação do aluno com base na média calculada
if med > 6:
  print("Aprovado")

elif med>5:
  print("Recuperação")
else:
  print("Reprovado")