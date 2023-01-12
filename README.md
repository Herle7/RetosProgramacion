# Solución de ejercicios Reto 1
Estas son las soluciones de algunos de los ejercicios de los retos propuestos, par ainiciar un proceso de vinculación y aprendizaje en algún(os) proyectos, determinando la etapa de cada participante

### Solución ejercico 4
El ejercicio 4 consta del siguiente enunciado:

*" Generar un arreglo con 20 números aleatorios de 1 a 100 y luego organizarlo de menor a mayor sin utilizar la sentencia `.sort()`"*


------------

Para solucionar este ejercicio, lo dividí en 3 segmentos:
1.  Crear el arreglo.
2. Generar un críterio para manipular ese arreglo.
3. Manipular el arreglo.

Para crear la el arreglo, utilicé la Biblioteca de ***Numpy***

######  Instalación Numpy:
Para poder utilizar esta biblioteca, realizamos su instalación por Terminal, ejecutando el siguiente comando:

   `pip install numpy`

Una vez hecho esto ya está disponible para importar en Python
	

##### Creación del arreglo:

Para crear una lista de números enteros, bajo un intervalo menor y uno mayor y el tamaño de la lista requerido, utilicé el siguiente metodo:
```python
	listaNumeros = np.random.randint(low=1, high=100, size=20).tolist() 
```
Una vez generada la lista, ahora tendremos que acceder a sus elementos.

#### Acceder a los elementos de la lista:

Para ello utilicé un `Map` doble, con la sentencia `for ` anidada, de la siguiente forma:

```python
	for numero1 in range(0 , len(listaNumeros)):
		for numero2 in range(numero1 + 1 , len(listaNumeros)): 
```
En donde accedemos a un primer elemento del arreglo y al elemento que le sigue a este, es decir, accedemos a dos elementos consecutivos en la lista.

Una vez accedí a los elementos de la lista, pude interactuar con estos, en este caso, mediante un criterio.

#### Establecer un criterio de manipulación:

El criterio de manipulación que empleé, responde  a sí el valor 'A' es mayor que el valor 'B', de esta forma: 
```python
	if (listaNumeros[numero1] > listaNumeros[numero2]): 
```
#### Manipulación del arreglo:
Al cumplirse el criterio establecido, ordenaremos los elementos, antemoniendo el valor menor al mayor, mediante la tecnica de asignación multiple, de esta forma:
```python
			listaNumeros[numero1] , listaNumeros[numero2] = listaNumeros[numero2] , listaNumeros[numero1]
```
