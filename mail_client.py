import smtplib, ssl
import os


folio_host = "smtp.gmail.com"
folio_port = 465

# CONNECTION
sender = os.getenv("DEVEM")
portfolio_key = os.getenv("EMKEY")
receiver = os.getenv("DEVEM")
folio_context = ssl.create_default_context()


def esend(message):

    with smtplib.SMTP_SSL(
        host=folio_host, port=folio_port, context=folio_context
    ) as server:
        server.login(sender, portfolio_key)
        server.sendmail(sender, receiver, message)
