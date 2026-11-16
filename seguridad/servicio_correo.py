import os
import smtplib
import ssl
from email.message import EmailMessage


def enviar_correo(destino: str, asunto: str, cuerpo: str) -> bool:
    usuario = os.getenv("SMTP_USER")
    clave = os.getenv("SMTP_PASS")
    if not usuario or not clave:
        if os.getenv("RECUPERACION_DEMO") == "1":
            print(" [DEBUG] Faltan SMTP_USER / SMTP_PASS")
        return False

    msg = EmailMessage()
    msg["From"] = usuario
    msg["To"] = destino
    msg["Subject"] = asunto
    msg.set_content(cuerpo)

    try:
        with smtplib.SMTP(os.getenv("SMTP_HOST", "smtp.gmail.com"),
                          int(os.getenv("SMTP_PORT", "587")), timeout=15) as servidor:
            servidor.starttls(context=ssl.create_default_context())
            servidor.login(usuario, clave)
            servidor.send_message(msg)
        return True
    except Exception as ex:
        print(f"  [!] No se pudo enviar el correo: {type(ex).__name__}: {ex}")
        return False