file1 = 'data/file1.txt'
file2 = 'data/file2.txt'
with open(file1, "r") as fistfile:
    content = fistfile.read().split('\n')

fisrtfile_list = [elements.split('\t') for elements in content]

with open(file2, "r") as secondfile:
    content = secondfile.read().replace(' ','\t').split('\n')
#print(content)
secondfile_list = [elements.split('\t') for elements in content]

print(secondfile_list) 
