import smtplib, ssl


folio_host = "smtp.gmail.com"
folio_port = 465

# CONNECTION
sender = "esDevmail72@gmail.com"
portfolio_key = "eyirswehplooyrmb"
receiver = "esDevmail72@gmail.com"
folio_context = ssl.create_default_context()


def esend(message):

    with smtplib.SMTP_SSL(
        host=folio_host, port=folio_port, context=folio_context
    ) as server:
        server.login(sender, portfolio_key)
        server.sendmail(sender, receiver, message)
