
#erro divisão por zero



n1 = 8
n2 = 3

try:
    r = n1/n2
except ZeroDivisionError:
    print("Não é possível dividir por 0")
else:
    print(r)
finally:
    print("fim do calculo")



