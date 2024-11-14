import streamlit as st
import pandas as pd
import smtplib
import ssl
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import time
#import os
#import schedule
#from google.oauth2 import service_account
#from googleapiclient.discovery import build
import random

st.set_page_config(page_title="Execução Mary 05")

with st.container():
        st.subheader("Inicio do script")
        # Configurações do email
        email_sender = 'mary@aknetworks.co'
        password_sender = 'FernandoRes@1'
        smtp_server = 'smtp.hostinger.com'
        smtp_port = 465
        bcc_email = 'fernando@i4sec.network'  # Email em cópia oculta
        # URL pública da planilha do Google Sheets
        SHEET_URL = 'https://docs.google.com/spreadsheets/d/1J-hxA5d1-40aJYIhQCffD0IqhyeyJQmdrX5YSh4SuC4/export?format=csv'
        
        # Função para enviar email
        def send_email(to_email, to_name):
            # Criação da mensagem
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = to_email
            msg['Subject'] = "Último contato da AK Networks"
            msg['Bcc'] = bcc_email  # Adiciona o BCC
        
            # Conteúdo HTML do email
            html_content = f"""
            <html>
                <body>
                    <p>Olá, {to_name}, tudo bem?<p>
                    <p>Esse será meu último email.</p>
                    <p>Gostaria de ressaltar que é muito importante possuir uma estratégia de segurança da informação e a solução de proteção de emails da PerceptionPoint é uma das melhores soluçôes para aumentar os níveis de segurança:</p>
                    <p>1. Detecta todos os tipos de ameaças (ATO, BEC, phishing, malware, ransomware, 0-Days...) em uma média de 20 segundos, enquanto os concorrentes levam em média 15 minutos.</p>
                    <p>2. Escaneamento de 100% do conteúdo. Maior taxa de detecção do mercado. </p>
                    <p>3. Serviço de resposta a incidentes disponível 24/7/365. Agindo como uma extensão do seu SOC </p>
                    <p>O que você acha de falarmos rapidamente sobre isso?</p>
                    <p>Muito obrigada!</p>
                </body>
            </html>
            """
            msg.attach(MIMEText(html_content, 'html'))

            # Envio do email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                server.login(email_sender, password_sender)
                server.sendmail(email_sender, [to_email, bcc_email], msg.as_string())
                print(f"Email enviado para {to_name} ({to_email}), com cópia oculta para {bcc_email}")
               
        # Loop para verificar e enviar emails
        while True:
            # Leitura da planilha usando pandas
            leads_df = pd.read_csv(SHEET_URL)
        
            # Data de hoje no formato DD-MM-AAAA
            today_date = datetime.now().strftime('%d/%m/%y')
        
            # Verifica cada lead e envia email se a data de hoje coincidir com a data de Envio_1
            for index, lead in leads_df.iterrows():
                
                # Define um intervalo aleatório entre 5 e 10 minutos (convertidos para segundos)
                intervalo_aleatorio = random.uniform(1 * 60, 2 * 60)
        
                first_name = lead['First_Name']
                email = lead['Email']
                envio_1 = lead['Envio_01']
        
                # Se a data de hoje for igual à data de Envio_1, envia o email
                if today_date == envio_1:
                    send_email(email, first_name)
        
                # Pausa a execução pelo intervalo scolhido
                time.sleep(intervalo_aleatorio)

                st.title("Executando script")    
            # Pausa o código por 24 horas antes de verificar novamente
            print("Verificação concluída. Aguardando até a próxima execução.")
            time.sleep(60)  # Pausa de 24 horas (86400 segundos)
        st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
        st.write("Fim")
