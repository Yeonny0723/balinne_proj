from balinne_website.googleEmail import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def custom_send_email(send_to, mail_subject, message):
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    # CLIENT_SECRET_FILE = dir_path + '/' + "client_secret.json"
    CLIENT_SECRET_FILE = "client_secret.json"
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = send_to
    mimeMessage['subject'] = mail_subject
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print('*email send successfully!',message)


