file1 = 'data/file1'
file2 = 'data/file2'
with open(file1, "r") as fistfile:
    list = fistfile.read().upper()
print(list)