import ast
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email notification
def send_noti(min_value, max_value):
    sender_email = 'mailertesta1@gmail.com'  # Replace with your email
    sender_password = 'pass1234?'         # Replace with your email password or app-specific password
    recipient_email = 'mailertesta2@gmail.com' # Replace with the recipient's email
    smtp_server = 'smtp.example.com'          # Replace with your SMTP server
    smtp_port = 587                          # Replace with your SMTP server's port (usually 587 for TLS)
    
    # Read from a .txt file
    try:
        with open('reagents.txt', 'r') as file:
            data_string = file.read()
    except FileNotFoundError:
        print('Error: The file "reagents.txt" was not found.')
        exit(1)

    # Convert the string to a dictionary
    try:
        reagents = ast.literal_eval(data_string)
        min_value = min(reagents.values())
        max_value = max(reagents.values())
        if not isinstance(reagents, dict):
            raise ValueError('The file does not contain a valid dictionary.')
    except (ValueError, SyntaxError):
        print('Error: Unable to convert the file content to a dictionary.')
        exit(1)
    try:
        min_value = int(min_value)
        max_value = int(max_value)
    except ValueError:
        print('Error: Unable to convert values to integers.')
        exit(1) 
    if min_value < max_value / 2:
        subject = "Alert: It's Time to Order More Reagents"
        body = f'Please order more reagents. Inventory has dropped below halfway point.'
    else:
        subject = 'No Alert'
        body = f'Plenty of Inventory.'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print('Email notification sent successfully.')
    except Exception as e:
        print('Email notification could not be sent. Error:', str(e))

# Read from a .txt file
try:
    with open('reagents.txt', 'r') as file:
        data_string = file.read()
except FileNotFoundError:
    print('Error: The file "reagents.txt" was not found.')
    exit(1)

# Convert the string to a dictionary
try:
    reagents = ast.literal_eval(data_string)
    print(reagents)
    min_value = min(reagents.values())
    max_value = max(reagents.values())
    if not isinstance(reagents, dict):
        raise ValueError('The file does not contain a valid dictionary.')
except (ValueError, SyntaxError):
    print('Error: Unable to convert the file content to a dictionary.')
    exit(1)
try:
    min_value = int(min_value)
    max_value = int(max_value)
except ValueError:
    print('Error: Unable to convert values to integers.')
    exit(1)

# Send an email notification if min < max / 2
send_noti(min_value, max_value)
