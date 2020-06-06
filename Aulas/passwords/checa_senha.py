import requests
import os
import hashlib
from getpass import getpass

url_api = 'https://api.pwnedpasswords.com/range/'
clear   = lambda: os.system('cls' if os.name=='nt' else 'clear') # função para limpar o console, testando se é Windows ou UNIX

def entrada_usuario():
    while True:
        try:
            entrada = int(input(f"Opções disponíveis:\n\n\t[1] - Para testar uma senha\n\t[2] - Para testar várias senhas, lendo-as de um arquivo TXT\n\t[3] - Para sair\n\nInforme a opção desejada: "))
            clear()
            if entrada == 1:
                senha = getpass(prompt="Informe sua senha \033[0;37;41m(Ela NÃO irá aparecer na tela)\033[0;37;40m: ")
                return senha
            elif entrada == 2:
                arq = input(f"Informe o caminho do Arquivo TXT: ").strip(r'"')
                return cria_lista_do_aquivo(arq)
            elif entrada == 3:
                return exit()
            else:
                clear()
                print("Huuummm.... parece que você não entendeu o menu...\n")
        except:
            clear()
            print(f"\nTente de novo com números, seu animal de teta...\n\n")

def retorna_sha1(senha):
    # Função de HASH necessita da string no formato de byte, por isso do uso do Método .ENCODE (existenten nas Strings)
    hash_object = hashlib.sha1(senha.encode())
    # Agora vamos converter o HASH de volta para STR, com caracters padrão UTF-8 em UPPER
    return hash_object.hexdigest().upper()

def busca_senha(str_sha1):
    """ API do HaveIBeenPwned usa o conceito de k-Anonymity e trabalha com apenas os 5 primeiros caracteres da senha em SHA-1 (HEAD)
        O Retorno da API são os demais caracteres de senha em SHA-1 (TAIL) 
        Função retorna uma Lista com o TAIL:Qtde_vazamentos ou retorna uma Lista Vazia.
    """
    res = requests.get(url_api + str_sha1[:5])
    if res.status_code == 200:
        # Decode necessário para converter de BYTE (retorno do objeto RES) para STR
        lista_tails = [ linha.decode("UTF-8") for linha in res.iter_lines() if linha.decode("UTF-8").split(':')[0] == str_sha1[5:] ]
        return lista_tails
    else:
        raise Exception(f"\nVerifique a API !!! \n\t Código de retorno da API: {res.status_code} \n")

def cria_lista_do_aquivo(arquivo):
    with open(arquivo, "r") as txt:
        lista_senhas = [line.rstrip('\n') for line in txt]
    return lista_senhas

def msg_saida(lista):
    if lista:
        return str(f"\nATENÇÃO:: senha digitada encontra-se nos dumps vazados.\n{'*'*3} Contagem de Vazamentos: {lista[0].split(':')[1]} \n{'*'*3} Você DEVE trocá-la o quanto antes...\n\n")
    else:
        return str(f"\nSenha não comprometida! Ela não está na base de dados do HaveIBeenPwned.\n\n")

def main():
    clear()
    print (f"\nScript em Python para checar se sua senha foi vazada e está nos dumps que o site HaveIBeenPwned disponibiliza. \nUsando a API v3 do site: https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange\n")
    input("Pressione ENTER para continuar...")
    clear()   
    userInput = entrada_usuario()
    if type(userInput) == str:
        pwned = busca_senha(retorna_sha1(userInput))
        print(msg_saida(pwned))
    elif type(userInput) == list:
        i = 0
        for senha in userInput:
            i += 1
            pwned = busca_senha(retorna_sha1(senha))
            print(f"\033[0;37;41mSenha da Linha {i} ==>\033[0;37;40m" + msg_saida(pwned), end="")
    return exit()

main()
