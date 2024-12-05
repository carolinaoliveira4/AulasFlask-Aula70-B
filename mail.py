import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Configurações do servidor SMTP
MAIL_SERVER = 'smtp.zoho.com'
MAIL_PORT = 587
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Substitua pelo seu e-mail Zoho
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Substitua pela sua senha Zoho
MAIL_SENDER = 'ygorslima@zohomail.com'

# Função para enviar o e-mail
def send_email(to, subject, body):
    # Criar a mensagem
    msg = MIMEMultipart()
    msg['From'] = MAIL_SENDER
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))  # Corpo do e-mail no formato texto simples

    # Conectar ao servidor SMTP e enviar o e-mail
    server = None  # Inicializa a variável server
    try:
        # Conectar ao servidor SMTP
        server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        server.starttls()  # Inicia o TLS (para segurança)

        # Fazer login no servidor SMTP
        server.login(MAIL_USERNAME, MAIL_PASSWORD)

        # Enviar o e-mail
        server.sendmail(MAIL_SENDER, to, msg.as_string())
        print(f'E-mail enviado para {to}')
    except Exception as e:
        print(f'Falha ao enviar e-mail: {e}')
    finally:
        if server:
            server.quit()  # Fechar a conexão com o servidor SMTP, se o servidor foi definido

# Enviar um e-mail de teste
if __name__ == '__main__':
    to_email = 'ygor.lima@bandtec.com.br'  # Substitua pelo e-mail do destinatário
    subject = 'Testando envio de e-mail'
    body = 'Este é um e-mail de teste enviado via Python com smtplib e Zoho SMTP.'
    send_email(to_email, subject, body)
