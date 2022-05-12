import argparse

arg_parser = argparse.ArgumentParser(description="Calcula el contenido de AT")
arg_parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)

arg_parser.add_argument("-o", "--output",
                    help="Path for the output file",
                    required=False)
         
arg_parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    required=False)

args = arg_parser.parse_args()

print(args)

with open(args.input, "r") as seq_file:
    my_dna = seq_file.read()
    
length = len(my_dna) 
a_count = my_dna.count('A') 
t_count = my_dna.count('T')

if args.round:
    at_content = round((a_count + t_count) / length, args.round)
    
else:
    at_content = (a_count + t_count) / length

with open("results/output_final.txt","w") as archivo_final:
    archivo_final.write(f"AT content is {str(at_content)}")

if args.output:
    print("La ruta del archivo final es: results/output_final.txt")

print("AT content is " + str(at_content))
    