#funções builtin

valores = [2,5,6,-2,0,11]
print(max(valores))
print(min(valores))



import math

# Número para os exemplos
num = 16
angle = math.radians(45)  # Convertendo 45 graus para radianos

# Raiz quadrada
raiz_quadrada = math.sqrt(num)
print(f'Raiz quadrada de {num} é {raiz_quadrada}')

# Fatorial
fatorial = math.factorial(5)
print(f'Fatorial de 5 é {fatorial}')

# Exponenciação
expo = math.pow(2, 3)
print(f'2 elevado a 3 é {expo}')

# Valor absoluto
absoluto = math.fabs(-10)
print(f'Valor absoluto de -10 é {absoluto}')

# Logaritmo natural (base e)
log_natural = math.log(num)
print(f'Logaritmo natural de {num} é {log_natural}')

# Logaritmo base 10
log_base10 = math.log10(num)
print(f'Logaritmo base 10 de {num} é {log_base10}')

# Seno
seno = math.sin(angle)
print(f'Seno de 45 graus é {seno}')

# Cosseno
cosseno = math.cos(angle)
print(f'Cosseno de 45 graus é {cosseno}')

# Tangente
tangente = math.tan(angle)
print(f'Tangente de 45 graus é {tangente}')

# Valor de pi
pi = math.pi
print(f'O valor de pi é {pi}')

# Valor de e
e = math.e
print(f'O valor de e é {e}')
