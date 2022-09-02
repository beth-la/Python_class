# Diccionarios

Para crear un diccionario en python: 

- Se crea por medio de llaves, declarando cuales serán las llaves (keys)  las cuales deben de  ser únicas. 

  ```
  enzymes = {
  'EcoRI': r'GAATT',
  'AvaII': r'GGCC'
  }
  
  Enzymes={}
  
  # Métodos
  
  #Elimina un elemento de un diccionario
  enzymes.pop('EcoRI')
  
  # Obtener elementos dentro de un diccionario:
  all_counts["key"]
  # Si esperamos que el elemento no se encuentra en el diccionario, entonces, podemos hacer que nos devuelva un 0.
  all_counts.get('TC',0)
  
  # Para obtener las llaves 
  all_counts.keys()
  
  # Función sort 
  sort(variable)
  
  # Metodo items: regresa tuplas, las llaves y el valor
  all_counts.items()
  
  # Ya que genera tuplas, entonces podemos iterar sobre ambos elementos.
  for key, item in all_counts.items:
  	Print(key)
  	print(item)
  	
  # fromkeys: inicializar un diccionario con valores e iterables: listas, tuplas, etc.
  llaves = [a,b,c,d]
  diccionario = dict.fromkeys(llaves,[])
  {'a':[],'b':[],...}
  
  # Por el contrario:
  llaves = [a,b,c,d]
  valores =[1,2,3]
  diccionario = dict.fromkeys(llaves,valores)
  {'a':[1,2,3],'b':[1,2,3],...}
  
  # Popitem: borra el ultimo par clave-valor insertado.
  diccionario.popitem()
  
  # setdefault: inserta un elemento al final del diccionario si es que este no fue encontrado y se asigna un valor "none"
  diccionario.setdefault("peso")
  
  # Values
  Accede a los valores 
  ```

  