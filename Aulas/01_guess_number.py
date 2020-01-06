from random import randint
from sys import argv

try:
    nr_start = int(argv[1])
    nr_end = int(argv[2])
except:
    nr_start, nr_end = None, None

while True:
    try:
        if nr_start == None:
            nr_start = int(input("Informe o número inicial: "))
        if nr_end == None:
            nr_end = int(input("Informe o número final: "))
        if nr_start < nr_end:
            break
        else:
            print("Hey man, o número inicial deve ser menor que o final...")
            nr_start, nr_end = None, None
    except:
        print("Por favor, informe apenas números, não caracteres de texto / inválidos...")

nr_secret = randint(nr_start, nr_end)

while True:
    try:
        # print(f"Dica de hoje: {nr_secret}")
        guess = int(input(f"Tente acertar o número secreto (entre {nr_start}~{nr_end}): "))
        if nr_start <= guess <= nr_end:
            if guess == nr_secret:
                print("Parabéns, vc acertou !!!")
                break
            else:
                print("Huummm, vc não acertou dessa vez... Tente novamente!")
        else:
            print(f"Hey man, eu disse entre {nr_start}~{nr_end}")
    except:
        print("Por favor, informe apenas números, não caracteres de texto ou inválidos...")
