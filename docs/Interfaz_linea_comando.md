# Interfaz de línea de comando

Argumentos a través de la línea de comandos en Python.

Python afmite 3 formas diferentes de manejar los argumentos de la línea de comandos.

- Utilizando el sys modulo 
- Getopt módulo que maneja las opciones tanto cotas como largas, incluida la evaluación de los valores de parametros.

## Modulo sys 

Toma los argumentos de la línea de comando y los guarda en una lista, cada elemento de la lista representa un solo argumento.

En la posición 0 de la lista se guarda siempre el nombre del archivo.

Guarda los argumentos en el orden en el que son dados.

## Tipos de argumentos 

- Posicionales: valor del argumento 
- Opcional

 ## argparse

Se necesita utilizar el método:

```
# Primeras fases para definir argparse 

parser = argparse.ArgumentParser()
parser.parse.args()

print (parser)
```

Ya tiene la opción de (-h) para help del programa. 

Tiene un atributo descripción para identificar que hace un programa 

```
import argparse

# Initiate the parser

parser = argparse.ArgumentParser(description="Este programa no hace nada")
parser.parse_args()
print (parser)
```

