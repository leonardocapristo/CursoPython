#dicionario são listas com index por nome

#chaves de dicionario podem ser string, int ou float

# "chave" : valor("texto", float ou int)


meuDicionario = {
    "nome":"Leo", 
    "idade": 22
    }

print(meuDicionario["nome"])
print(meuDicionario["idade"])

print(meuDicionario.keys())
print(meuDicionario.values())
print(meuDicionario.items())


#adicionar um item no dicionario

meuDicionario["sobrenome"] = "Capristo"
print(meuDicionario)

#excluir item do dicionário
del meuDicionario["sobrenome"]
print(meuDicionario)