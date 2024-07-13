nome = "Leo"
idade = 22


#concatenar strings e números usar vírgula "," se usar o "+" vai bugar
# print("sua idadade é : " + idade)

print("sua idadade é : ", idade)

msgUsandoFormat = "Olá {} tudo bem ? você tem {} anos usando .format".format(nome,idade)

msgUsandoF = f"Olá {nome} tudo bem ? você tem {idade} anos usando f'string'"


print( "Olá {} tudo bem ? você tem {} anos usando .format".format(nome,idade) )

print( f"Olá {nome} tudo bem ? /n você tem {idade} anos usando f'string'" )

print(msgUsandoF)
print(msgUsandoFormat)