# Expresiones regulares 

```
import re
re. search("patron","a buscar")
re.search("GGG","GGGGGG")

```

En las expresiones regulares:

-  "." cualquier carácter.

- [AT] cualquiera de las letras que se encuentren dentro de los corchetes, operador de conjunto. 

- (A|T) cualquiera de las opciones separadas por pipes. 

- [^] negación.

- ? Un carácter puede estar 0 o 1 vez 

- "+" una o más veces 

- "*" 0 o más veces 

- {número} o {numero, numero} cuando sabemos el número de ocurrencias de cierto patrón.

- ^ indica también cuando se busca que cierto patrón sea el inicio. 

-  $ final de una cadena

  .span metodo que guarda las coordenadas de donde se hizo match 

  .group la cadena que se busco 

  .string la cadena en la que se busco 

  .group para acceder a los elementos capturados.

  () para capturar match 