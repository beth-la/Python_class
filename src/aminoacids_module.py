'''
Module name
    Aminoacids module

Description 
    Modulo que contiene funciones que nos permiten trabajar con secuencias de nucleotidos.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.

Functions
    aminoacid_per
    
''' 

def aminoacid_per(aminoacid_sequence, aminoacid_list = ['A','I','L','M','F','W','Y','V']):
    '''
    Calcula el porcentaje de aminoacidos en una seuencia 
        Parameters:
            aminoacid_sequence (str): secuencia de aminoacidos dada por el usuario
            aminoacid_list (list): aminoacidos a calcular el porcentaje, por default ['A','I','L','M','F','W','Y','V']
        
        Returns:
            percentage (float): porcentaje de aminoacidos 
    '''
    
    length = len(aminoacid_sequence)
    aminoacid_count = 0
    
    for i in range(0,len(aminoacid_list)):
        aminoacid_count += str(aminoacid_sequence).upper().count(str(aminoacid_list[i]).upper())
        
    percentage = (aminoacid_count * 100)/ length
    
    return(percentage)
