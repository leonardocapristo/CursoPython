lista = [1,2,3,4,5,6,7,8,9]

for numero in lista:
    print(numero)


print("    ")

texto = "Banana"
for letra in texto:
    print(letra)


#se precisar rodar o comando for em "x" vezes usar o comando range :

senha = "Leo123"
campoSenha = input("Digite sua senha : ")

for tentativaSenha in range(3):
    if (campoSenha == "Leo123"):
        print("login feito com sucesso")
        break
    else:
        print("Senha invalida tente novamente")
        campoSenha = input("Digite sua senha : ")


pedras = ["rubi", "esmeralda", "quartzo", "diamante"]

for pedra in pedras:
    print(pedra)

