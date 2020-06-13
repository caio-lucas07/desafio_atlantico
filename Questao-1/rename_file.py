import os
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()
print(args)

def rename(diret):
    
    
    
    diretorio = diret
    i = 1
    
    for name in os.listdir(diretorio):
        
        filename, file_extension = os.path.splitext(name)
        
        if (file_extension == 'ini'):
            break
        else:
            src = str(name)
            novo_nome = str(str(i) + file_extension)
            os.rename((diretorio+src), (diretorio+novo_nome))
            i += 1
            print("arquivo " + name + " alterado para " + novo_nome)
        
    
rename('./arquivos/') 
