# Modulo de aminoacidos 

def aminoacid_per(aminoacid_sequence, aminoacid_list = ['A','I','L','M','F','W','Y','V']):
    
    '''
    Returns the percentage of aminoacids in a sequence 
        Parameters:
            aminoacid_sequence (str): sequence of aminoacids given by the user 
            aminoacid_list (list): aminoacids to calculate the percentage, by default ['A','I','L','M','F','W','Y','V']
        
        Returns:
            percentage (float): aminoacids percentage 
    '''
    
    length = len(aminoacid_sequence)
    aminoacid_count = 0
    
    for i in range(0,len(aminoacid_list)):
        aminoacid_count += str(aminoacid_sequence).upper().count(str(aminoacid_list[i]).upper())
        
    percentage = (aminoacid_count * 100)/ length
    
    return(percentage)

def aminoacid_per(aminoacid_sequence, aminoacid):
    
    '''
    Returns the percentage of aminoacids in a sequence 
        Parameters:
            aminoacid_sequence (str): sequence of aminoacids given by the user 
            aminoacid_list (str): aminoacid to calculate the percentage
        
        Returns:
            percentage (float): aminoacid percentage 
    '''
    
    sequence_length = len(aminoacid_sequence)
    percentage = (aminoacid_sequence.upper().count(aminoacid.upper()) * 100)/ sequence_length
    return(percentage)