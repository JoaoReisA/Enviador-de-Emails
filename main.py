import smtplib, ssl, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from lista_email import retorno_email
from retorno_html import retorno_html

print('-------Bem vindo ao enviador de emails automático-------')
emailuser = "SEU EMAIL"
password = "SUA SENHA"
port = 465
assunto = 'URGENTE: Você precisa organizar a sua vida financeira hoje!'
msg = MIMEMultipart("alternative")
msg['From'] = emailuser
msg['To'] = 'Cliente'
msg['Subject'] = assunto
sslcontext = ssl.create_default_context()
connection = smtplib.SMTP_SSL("smtp.gmail.com", port, context=sslcontext)


def send_email():
    email_cliente = retorno_email()
    cont = 0
    connection.login(emailuser, password)
    for i in range(0, len(email_cliente)):
        connection.sendmail(emailuser, email_cliente[i], text)
        cont += 1
        print(cont)
        time.sleep(0)
    print(f'A quantadidade de emails enviada foi: {cont}')


inicar = input('Deseja iniciar o programa (S) ou (N): ')
if (inicar.upper().strip() == 'S'):
    try:
        print('Começando o envio...')
        plain_send = '''
        Oi Como você está?
        '''
        msg.attach(MIMEText(plain_send, 'plain'))
        body = retorno_html()
        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        send_email()
    except:
        print('Não foi possível concluir a operação')
        input('Digite uma tecla para finalizar: ')
    finally:
        connection.quit()
        print('O programa foi finalizado')
else:
    print('Não foi possível iniciar a operação')
