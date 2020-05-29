import os
from sys import argv
from PIL import Image

# Carrega em VAR os argumentos da chamada do script
try:
    origem = argv[1]
    destino = argv[2]
    print(f"{origem}, {destino}")
except:
    origem, destino = None, None

if origem == None:
    origem = r'C:/pokedex/'
if destino == None:
    destino = r'C:/pokedex/new/'

# Cria a pasta se não existir
if not os.path.isdir(destino):
    os.mkdir(destino)

# Faz a leitura dos filhos da pasta, e cria uma lista caso o item seja arquivo "os.path.isfile"
with os.scandir(origem) as entries:
    arquivos = [entry.name for entry in entries if os.path.isfile(origem + entry.name)]


# Iterração para converter cada item encontrado
for a in arquivos:
    img = Image.open(origem + a)
    out = destino + a.replace("jpg", "png")
    img.save(out)
    print("All Done!")

