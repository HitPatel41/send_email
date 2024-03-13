import os
import base64
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

load_dotenv()
api_key = os.getenv('SENDGRID_API_KEY')
if not api_key:
    raise ValueError("API key not found in environment variables.")

message = Mail(
    from_email='Parth <no-reply@parth2success.com>',
    to_emails='dalsaniyahit@gmail.com',
    subject='This is the testing subject from Parth',
    html_content='<strong>This is the testing content of mail from Parth</strong>'
    )

# Condition to decide whether to send an attachment
send_attachment = True

if send_attachment:
    # Your file path here
    file_path = 'C:\\Users\\BAPS\\Pictures\\Screenshots\\Screenshot (1).png'

    # Read and encode file content in base64
    with open(file_path, 'rb') as f:
        file_content = f.read()
    encoded_file = base64.b64encode(file_content).decode()

    attachment = Attachment()
    attachment.file_content = FileContent(encoded_file)
    attachment.file_type = FileType('application/png')  # Mime type
    attachment.file_name = FileName('screenshot.png')  # The name of the file that will be displayed in the email
    attachment.disposition = Disposition('attachment')  # Attachment or inline
    attachment.content_id = 'screenshot'  # Use if you want the file to be accessible using a Content-ID in HTML

    # Add the attachment to your message
    message.add_attachment(attachment)

try:
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
