 #acessar letra da string
nome = "Leonardo"
frase = "Leonardo está aprendendo a programar em python"

letraInicial = nome[0]

print(letraInicial)

#separando a string por palavras

palavras = frase.split()

print(palavras)

#pegando string de um ponto até outro ponto

print(frase[0:5])

#procurando email

email = input("Digite seu endereço de email: ")
arroba = email.find("@")
print(arroba)

usuario = email[0:arroba]
dominio = email[arroba:]

print(dominio)


#verificando se palavras estão na string, retorna true ou false

texto = "bicarbonato de sódio e óxido de zinco"
print("sódio" in texto)
print("magnésio" not in texto)


#deixando string toda em maiúscula

print(nome.upper())

