import csv
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization

# Dirección de correo electrónico y API Key de SendGrid
SENDGRID_API_KEY = 'SendGrip API Key'
FROM_EMAIL = 'test@example.com'

# Leer las direcciones de correo electrónico de destinatario desde un archivo CSV
def read_recipients(file_name):
    recipients = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            recipients.append(row[0])
    return recipients

# Leer el cuerpo del mensaje desde un archivo de texto
def read_message_body(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# se crea una instancia de sendgrid.SendGridAPIClient
def main():
    recipients = read_recipients('recipients.csv')
    message_body = read_message_body('message.txt')

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

# Se envían los correos a cada destinatario utilizando un bucle for
    for recipient in recipients:
        mail = Mail(
            from_email=Email(FROM_EMAIL),
            subject='Test Message',
            plain_text_content=Content('text/plain',message_body)
        )
        
        personalization = Personalization()
        personalization.add_to(Email(recipient))
        mail.add_personalization(personalization)

# Si el envío del correo falla, se imprimirá un mensaje de error.
        try:
            response = sg.send(mail)
            print('Email sent to', recipient)
        except Exception as e:
            print('Failed to send email to', recipient)
            print(e)

if __name__ == '__main__':
    main()
