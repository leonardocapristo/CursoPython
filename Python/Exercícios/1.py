
# Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deve calcular e mostrar:
# a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.


custo = float(input("Digite o custo do espetáculo: "))
convite = float(input("Digite o preço do convite: "))

vendaMinima = custo / convite
print(f"é necessário vender no mínimo {vendaMinima} convites")

vendaMinimaLucro = vendaMinima * 1.23

print(f"para ter um lucro de 23% é necessário vender {vendaMinimaLucro} bilhetes")
