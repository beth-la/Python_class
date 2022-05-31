# Expresiones regulares 

Patrones:

Se hablan de regularidades. Un patrón es una sucesión de elementos que se construye siguiendo una regla al observar las regularidades. 

Patrones de búsqueda dentro de formatos bioinformáticos  

```
# Modulo de expresiones regulares en Python
import re
```

​	Búsqueda de patrones en un string:

Algunas veces se tiene que buscar más de un objeto con un mismo patrón con una expresión regular.

GGXCC "X" puede ser A o T -> GG(A|T)CC

GGXCC "X" puede ser A o T -> GG[AT]CC

Regexp [^] Para negar caracteres especificos 

Regexp? Toma una o cero veces el carácter  

![image-20220526123430739](C:\Users\Brenda Elizabeth L\AppData\Roaming\Typora\typora-user-images\image-20220526123430739.png)

