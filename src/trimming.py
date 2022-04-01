with open('data/4_input_adapters.txt','r') as archivo:
    secuencias= [line.split("\n") for line in archivo]
    print(secuencias[0][0:14])