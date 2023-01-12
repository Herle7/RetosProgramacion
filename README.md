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

------------

####  Solución ejercicio 2:

El enunciado para este ejercicio es el siguiente:

*Crear un input (o prompt de entrada) donde se ingrese un año y determina si es bisiesto en el calendario gregoriano.*

Para poder re solver este ejercicio, primero tuve que entender las caracteristicas de un año bisiestro, a lo cual encontre que:

> Un año es bisiesto si es divisible entre 4, excepto si es divisible entre 100. Sin embargo, si es divisible entre 400, entonces sí es bisiesto.

Siguiendo esta premisa, tendría que realizar una evaluación del año:
1.  ¿Es divisible entre 4?
2. No puede ser divisible entre 100.
3. Es divisble entre 400 pero no entre 100.

para ello planteé la siguiente linea de `if`:

```python
if year % 4 = 0 and ( year % 100 != 0  or year % 400 = 0):
```
Si cumple con las condiciones anidadas de esta linea de comando, el año  es bisiestro.

Para resolver las indicaciones del ejercicio, entonces solo bastaría con realizar el comando `input` y mostrar los mensajes en pantalla con el metodo `print`, pero  hay que tener en cuenta algo.

```python
year = int(input("ingrese el año que desea evaluar: ")) 
```
Tendía que convertir el valor en un entero para poder realizar la operación de `%`  correctamente, que lo que hace es revisar el sobrante de la división. Por lo cual usamos el metodo de conversión `int()`

Y finalizando el código, agregué una metodo `try` `and` `except`, en caso de que el usuario ingresara un valor erroneo, no se 'rompiece' la ejecución del programa.

Por lo cual el código final es el siguiente:

```python
year=input("Ingrese el año que desea evaluar, ejemplo 1998: ")
try:
    year = int(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('El año',year, "es bisiesto.")
    else:
        print('El año',year, "no es bisiesto.")    

except:
    print('No ingreso un valor valido')
    exit()
```












