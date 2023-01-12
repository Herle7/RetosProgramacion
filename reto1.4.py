'''
Generar un arreglo 
con 20 números aleatorios de 1 a 100
y luego organizalos de menor a mayor
'''
import numpy as np # importamos la librería de numpy


listaNumeros = np.random.randint(low=1, high=100, size=20).tolist() # generamos números aleatorios entre 1 y 100 y los convertimos en una lista

print(listaNumeros)
print(f'\n---------------------------------------')
for numero1 in range(0,len(listaNumeros)): # recorremos la lista que generamos
    for numero2 in range(numero1+1,len(listaNumeros)): # recorremos la lista en una posición adelantada a la anterior
        if (listaNumeros[numero1]>listaNumeros[numero2]): # comparamos los elementos de los recorridos
            listaNumeros[numero1],listaNumeros[numero2] = listaNumeros[numero2],listaNumeros[numero1]
        #intercambiamos las posiciones de los elementos en caso de que se cumpla la condición 

print(listaNumeros)    


            