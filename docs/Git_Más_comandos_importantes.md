# Git: Más comandos importantes.

*17 de febrero 2022*

Comandos importantes para modificación de archivos en git:

Para obtener cada uno de los commits realizados en el repositorio en orden cronológico inverso, también da el autor.

--N arroja la cantidad indicada de commits a devolver

--online devuelve una versión reducida de información, da un identificador corto de los commits 

--author 

```
git log
git log --N
git log --oneline
git log --author= "nombre"
```

Diferencia entre archivos editados 

--staged señala cambios que están en área de preparación 

```
get diff
get diff --staged
```

Para obtener que archivos fueron modificados, eliminados o agregados a nuestro repositorio:

-u nos muestra más a detalle 

```
git status 
git status -u 
```

Modificar mensaje de un commit realizado: No es recomendable ya que cambia el ID del commit 

```
git rebase --interactive [ID commit]^
reword [ID commit][mensaje de commit]
```

Cada commit se apila uno encima de otro, su posición en la cabecera cambia. El ultimo commit hecho se encuentra en la "cima" de la pila:

HEAD     Commit 3 (ultimo)

HEAD~1 Commit 2

HEAD~2   Commit 1

```
#Diferencia entre cabeceras
git diff HEAD [archivo]
git show HEAD~(numero) [archivo]
```

Restaurar una versión:

```
git checkout [HEAD/ID commit] archivo.py
```

