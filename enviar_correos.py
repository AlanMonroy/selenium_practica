import smtplib
from email.message import EmailMessage
import ssl

def enviar_correo():
    correo_emisor = 'alanmonroyzz99@gmail.com'
    password = 'pzdqtcddkwubtmpe'
    correo_receptor = 'roberto.rodriguez@grupotimexico.com'

    nombre = 'Roberto Alan Rodriguez Monroy'

    # Datos de correo
    asunto = 'Acceso a Alere QA'
    cuerpo = f'Buenos dias {nombre}'

    # Cuerpo del correo electrónico
    mensaje = EmailMessage()
    mensaje['From'] = correo_emisor
    mensaje['To'] = correo_receptor
    mensaje['Cc'] = 'alanmonroyzz99@gmail.com'
    mensaje['Subject'] = asunto
    mensaje.set_content(cuerpo)

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto) as envio_correo:
        envio_correo.login(correo_emisor,password)
        envio_correo.sendmail(correo_emisor,correo_receptor,mensaje.as_string())

enviar_correo()
