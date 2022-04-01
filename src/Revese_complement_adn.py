with open ('data/dna.txt','r') as archivo:
    
    adn= archivo.read()
    adn_lista= list(adn)
    adn_lista.reverse()
    complemento = []
    
    print(f"El reverso de la secuencia {adn} es {''.join(adn_lista)}")
    
    for nucleotido in list(adn):
        if nucleotido == 'A':
            complemento.append('T')
        if nucleotido == 'T':
            complemento.append('A')
        if nucleotido == 'G':
            complemento.append('C')
        if nucleotido == 'C':
            complemento.append('G')
                    
    print(f"El complemento de la secuencia {adn} es {''.join(complemento)}")