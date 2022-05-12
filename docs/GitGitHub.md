# Git y Git Hub 

Restaurar versiones:

```
git checkout 
```

Ignorar archivos: Es necesario crear un archivo llamado .gitignore, en donde se incluyen los archivos que se desean ignorar.

.gitignore

Este comando nos dice que archivos o directorios están siendo ignorados por git 

```
git status --ignored
```

Para decir que ignore todos menos uno:

```
#Ignora todo lo que sea extensión .data menos el archivo final.data
*.data 
!final.data 
```

