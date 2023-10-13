import ast
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_noti(min_value, max_value):
    sender_email = 'mailertesta1@gmail.com'  
    sender_password = 'eipfbfmothdbhexo'         
    recipient_email = 'bobbot33@outlook.com' 
    smtp_server = 'smtp.gmail.com'          
    smtp_port = 587                              
    try:
        with open('reagents.txt', 'r') as file:
            data_string = file.read()
    except FileNotFoundError:
        print('Error: The file "reagents.txt" was not found.')
        exit(1)
    try:
        reagents = ast.literal_eval(data_string)
        min_value = min(reagents.values())
        max_value = max(reagents.values())
        print(min_value)
        
        if not isinstance(reagents, dict):
            raise ValueError('The file does not contain a valid dictionary.')
    except (ValueError, SyntaxError):
        print('Error: Unable to convert the file content to a dictionary.')
        exit(1)
    try:
        min_value = int(min_value)
        max_value = int(max_value)
        print(min_value)
        
    except ValueError:
        print('Error: Unable to convert values to integers.')
        exit(1) 
    if min_value > (max_value / 2):
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
try:
    with open('reagents.txt', 'r') as file:
        data_string = file.read()
except FileNotFoundError:
    print('Error: The file "reagents.txt" was not found.')
    exit(1)
try:
    reagents = ast.literal_eval(data_string)
    min_value = min(reagents.values())
    max_value = max(reagents.values())
    print(min_value)
    
    if not isinstance(reagents, dict):
        raise ValueError('The file does not contain a valid dictionary.')
except (ValueError, SyntaxError):
    print('Error: Unable to convert the file content to a dictionary.')
    exit(1)
try:
    min_value = int(min_value)
    max_value = int(max_value)
    print(min_value)
    
except ValueError:
    print('Error: Unable to convert values to integers.')
    exit(1)
send_noti(min_value, max_value)
