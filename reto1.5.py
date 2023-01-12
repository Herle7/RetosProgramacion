
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


A = [random.choice(letras) for i in range(10)]
B = [random.choice(letras) for i in range(10)]

print(A)
print('-------------------------------')
print(B)
##### Union:

C = set(A) | set(B)
print("Unión: ", C)

##### Intersección:

C = set(A) & set(B)
print("Intersección: ", C)

##### Diferencia:

C = set(A) ^ set(B)
print("Diferencia: ", C)


diferencia_simetrica = set(A) - set(B)
print("Diferencia Simétrica: ", diferencia_simetrica)








