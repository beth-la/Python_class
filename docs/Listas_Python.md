# Listas en Python 

- Una lista puede contener caracteres/ números/ strings 

- Son mutables por lo que pueden ser modificadas 

- Para definir lista se usan corchetes 

  ```
  # Regresa el tipo de objeto de la variable 
  type(variable)
  ```

- Acceder a elementos de una lista:

  ```
  # Lista de una sola dimensión 
  lista[i]
  # Para listas de listas 
  lista[i][j]
  # Para rangos:
  listas[0:3]
  ```

- len(lista) funciona para listas y para strings 
- Concatenar listas con el operador "+"
- .index nos da el índice del elemento que buscamos:

```
lista.index("Arremangalarempujala")
```

- .append agrega elementos al final de la lista. 

- .extend() nos sirve para agregar elementos de una lista a otra lista, pero los agrega uno por uno y no se inserta una lista en otra lista. Por lo tanto la longitud de la lista aumenta con la cantidad de elementos de la lista agregada.
- . reverse() voltea la lista 
- sort() ordena por orden alfabético
- .split() permite generar una lista usando delimitadores de una cadena.  