from translate import Translator

translator = Translator(to_lang="it", from_lang='pt-br')

with open(r"C:\Users\Francis\Desktop\py\ZTM_Python\Aulas\traducao.txt") as arquivo:
    print(arquivo.read())
    arquivo.seek(0)
    print(translator.translate(arquivo.read()))

