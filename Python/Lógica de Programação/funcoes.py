#função sem argumento

def mostraOlaMundo ():
    print("Olá mundo !!!")

mostraOlaMundo()


#função com argumento

# O return salva o resultado da função para ser usada posteriormente

#Ex:

def somaDoisNumeros(n1,n2):
    return n1 + n2

numero1 = 2
numero2 = 4

resultado = somaDoisNumeros(numero1, numero2)

print(resultado)
print(somaDoisNumeros(numero1,numero2))


# função com 2 returns

def divideDoisNumeros(a,b):
    if (a and b != 0):
        return a/b
    else:
        return "impossível dividir por zero"

a = 6
b = 3

print(divideDoisNumeros(a,b))