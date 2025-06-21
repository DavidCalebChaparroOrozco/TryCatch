import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configura tu cuenta de correo (se recomienda usar variables de entorno)
EMAIL = "tu_correo@gmail.com"
PASSWORD = "tu_contraseña"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Firma personalizada
signature = """
Cordialmente,<br><br>
Julián Darío Luna Patiño
| ☁️ AWS Community Builder | Aprender haciendo 👨‍💻 | JavaScript 🫶🏻 | ✉️ judlup@trycatch.tv | oferti.co | Cloud Solutions Architect Lead @ Rena Ware | 
Colombia<br>
📧 tucorreohermano@gmail.com
"""

def send_emails_from_excel(excel_file):
    # Leer el archivo Excel
    df = pd.read_excel(excel_file)

    # Iniciar conexión con el servidor SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)

        # Recorrer cada fila del archivo
        for index, row in df.iterrows():
            route = row['Ruta']
            name = row['Nombre']
            recipient_email = row['Correo']

            # Crear mensaje
            subject = f"Información sobre tu ruta asignada"
            body = f"""
            <p>Estimado/a <b>{name}</b>,</p>

            <p>Te informamos que tu número de ruta asignado es: <b>{route}</b>.</p>

            <p>Por favor, revisa y confirma recepción de este mensaje.</p>

            {signature}
            """

            # Crear mensaje MIME
            message = MIMEMultipart("alternative")
            message["From"] = EMAIL
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "html"))

            try:
                server.sendmail(EMAIL, recipient_email, message.as_string())
                print(f"✅ Correo enviado a: {name} <{recipient_email}>")
            except Exception as e:
                print(f"❌ Error al enviar a {recipient_email}: {e}")

# Ruta al archivo Excel
excel_file = "destinatarios.xlsx"
send_emails_from_excel(excel_file)