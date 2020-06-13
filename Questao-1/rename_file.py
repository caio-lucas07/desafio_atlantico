import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('--input', metavar='i', type=str,
                    help='pasta com arquivos')

args = parser.parse_args()
print(args.input)

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
        
    
rename(args.input) 
