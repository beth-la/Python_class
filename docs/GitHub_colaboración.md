# GitHub: Un ambiente de colaboración

*Clase 5: 3 marzo 2022*

Enlazar un repositorio:

```
git remote add origin 
git remote -v
```

¿Como subir archivos locales al repositorio remoto?

```
git push origin master
```

Recordemos que git no controla carpetas sino documentos.

Traer archivos modificados de forma remota:

```
git pull origin master
```

Comando para visualizar un archivo:

```
cat nombre_de_archivo
```

Para hacer llegar propuestas de mejoras a repositorios de personas en GitHub:

pull request es una petición para integrar nuestras propuestas o cambios de código a un proyecto.

```
pull request 
```

Puedes modificar el código o documentos de más personas para agregar propuestas de mejoras, al hacerlo se genera una copia de los archivos y se notifica al dueño del repositorio, de esta forma este decide si lo acepta o no. 