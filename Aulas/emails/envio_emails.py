import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path   # Similar os.path

 
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = '<to email address>
email['subject'] = 'You won 1,000,000 dollars!'

# A função Template, permite trocar palavras chaves, representadas por um $ por outros valores.
### Deve ser informado no formato de dicionário, usando {} para responder o De-Para.
# Ao final, o método SET_CONTENT precisa informar que é no formato HTML o contúdo lido, do contrário ele não interpreta os comandos do arquivo.
email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<your email address>', '<your password>')
    smtp.send_message(email)
    print('all good boss!')

