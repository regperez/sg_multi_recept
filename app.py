import csv
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization

# SendGrid email address and API Key
SENDGRID_API_KEY = 'SendGrip API Key'
FROM_EMAIL = 'test@example.com'

# Read recipient email addresses from a CSV file
def read_recipients(file_name):
    recipients = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            recipients.append(row[0])
    return recipients

# Read the message body from a text file
def read_message_body(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# A SendGrid instance is created. SendGridAPIClient
def main():
    recipients = read_recipients('recipients.csv')
    message_body = read_message_body('message.txt')

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

# Emails are sent to each recipient using a for loop
    for recipient in recipients:
        mail = Mail(
            from_email=Email(FROM_EMAIL),
            subject='Test Message',
            plain_text_content=Content('text/plain',message_body)
        )
        
        personalization = Personalization()
        personalization.add_to(Email(recipient))
        mail.add_personalization(personalization)

# If the mail delivery fails, an error message will be printed.
        try:
            response = sg.send(mail)
            print('Email sent to', recipient)
        except Exception as e:
            print('Failed to send email to', recipient)
            print(e)

if __name__ == '__main__':
    main()
