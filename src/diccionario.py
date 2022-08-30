# Diccionarios 

cadena=[]
cadena= input("Introduce el texto que desees, no mas de 10000 letras \n") 

lista=cadena.split(' ') 
diccionario={}
sinEspacios= cadena.replace(" ","")

if len(sinEspacios) <= 10000:
  for word in lista:
    cuenta= lista.count(word)
    diccionario[word]= cuenta

  for word, valor in diccionario.items():
    print(word, end=' '),
    print(valor)
else:
  print("El texto no debe contener más de 10000 letras")