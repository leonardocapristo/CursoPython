minhaLista = [1,2,3]

print(minhaLista)

print(minhaLista[1])


#listas podem ter outros tipos primitivos dentro
minhaLista2 = [1 , 2.2 , "texto", True]

print(minhaLista2)

print(type(minhaLista2[0:2]))

# .append()     adiciona um novo elemento na lista

minhaLista3 = [1,2,3]
minhaLista3.append("adicionando texto")
print(minhaLista3)


juncao = minhaLista + minhaLista2
print(juncao)