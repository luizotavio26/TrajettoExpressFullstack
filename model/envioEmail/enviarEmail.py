# eftk pcui yzly ezmi   => não perde essa senha

import os
import smtplib
from email.message import EmailMessage
import mimetypes
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

remetente = "trajetoexpress04@gmail.com"
destinatario = "trajetoexpress04@gmail.com"
assunto = "Seu relatório chegou"  # Corrigido o typo em "assuto"
mensagem = """
Olá, aqui está o relatório com os dados de vendas.
"""

# Use variáveis de ambiente para dados sensíveis
senha = os.getenv("EMAIL_PASSWORD")

# senha = "ncgb owvx pyti ezcg"


# Use caminho absoluto para o arquivo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
anexo = os.path.join(diretorio_atual, "texto.txt")

try:
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    msg.set_content(mensagem)

    if os.path.exists(anexo):
        mime_type, _ = mimetypes.guess_type(anexo)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(anexo, 'rb') as arquivo:
            msg.add_attachment(
                arquivo.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=os.path.basename(anexo)
            )
    else:
        print(f"Arquivo não encontrado: {anexo}")
        exit(1)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(remetente, senha)
        email.send_message(msg)

    print("Email enviado com sucesso!")

except Exception as e:
    print(f"Erro ao enviar email: {str(e)}")