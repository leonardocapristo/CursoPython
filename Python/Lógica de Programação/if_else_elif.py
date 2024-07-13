nota1 = nota2 = 0.0

media =0.0

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))


media = (nota1 + nota2) / 2


if (media >=7):

    print("aprovado")

elif(media < 7 and media >= 1):

    print("pelo menos não tirou zero")

else:
    
    print("tirou 0 ! reprovado !")
