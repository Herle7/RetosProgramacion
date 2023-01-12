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


------------

####  Solución ejercicio 5:
El ejercicio 5 consta del siguiente enunciado :

*"Generar dos arreglos **A** y **B** con 10 valores aleatorios de letras del abecedario y mostrar los siguientes resultados: *

*1. Unión: A⋃B*
*2. Intersección A⋂B*
*3. Diferencia: AΔB*
*4. Diferencia Simétrica: A – B*

##### Solución:
Primero, realicé la importación de la biblioteca` random`.

Segundo establecí los elementos del conjunto `A` y `B`

```python
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```
Una vez establecido esto, procedí a crear una lista aleatoria con los elementos de cada conjunto:

```python
A = [random.choice(letras) for i in range(10)]
B = [random.choice(letras) for i in range(10)]
```
el metodo `choice` permite elegir elementos existentes de una lista, de manera aleatoria, es como si realizara un `for` para recorrer la lista y extrae los elementos de esta.

Para realizar las operaciones indicadas, utilicé el metodo `set` el cual permite realizar una representación de los conjuntos en **`Python`**

##### Union:
Utilizamos el operador  `|` que nos devuelve los elementos existentes en `A` y en `B`.
```python
C = set(A) | set(B)
print("Unión: ", C)
```
##### Intersección:
Utilizamos el operador  `&` que nos devuelve los elementos que existan tanto en `A` como en `B`.
```python
C = set(A) & set(B)
print("Intersección: ", C)
```
##### Diferencia:
Utilizamos el perador bit a bit `^` 
```python
C = set(A) ^ set(B)
print("Diferencia: ", C)
```
##### Diferencia simetrica:
Utilizamos el operador aritmetico `-` 
```python
C = set(A) - set(B)
print("Diferencia Simétrica: ", C)
```







