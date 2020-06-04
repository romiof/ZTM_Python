from bs4 import BeautifulSoup
import requests

res = requests.get(url='http://www.sazi.com.br/')

# print(res.content)
sopa = BeautifulSoup(res.content, 'html.parser')

print (sopa)
# print (sopa.prettify())


