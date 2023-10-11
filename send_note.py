#The function will search through the list and select the lowest number. If the number is lower than half of the highest value, it will send an email to notify the user to order more inventory.
#This function converts a string to a dictionary
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ast

#senders email.
sender_email = 'notificationbot@gmail.com'
sender_password = 'your_password'

#recipient's email address
recipient_email = 'whackett@pacificbiosciences.com'

#SMTP server settings
smtp_server = 'smtp.pacificbiosciences.com'
smtp_port = 587 # Port for TLS

msg = MIMEMultipart()

msg['From'] = sender_email
msg['To'] = recipient_email

msg['Subject'] = 'Order Reagents Notification'

body = 'Its time to order more reagents!'
msg.attach(MIMEText(body, 'plain'))

# Define a string representing a dictionary
def str2dict():
    with open('reagents.txt') as file_object:
        contents = file_object.read()
        string_dict = contents

# Use ast.literal_eval to convert the string to a dictionary
    try:
        dictionary = ast.literal_eval(string_dict)
        min_val = min(dictionary.values())
        max_val = max(dictionary.values())
        if isinstance(dictionary, dict):
            print("Successfully converted string to dictionary:")
            print(dictionary)

        else:
            print("The string did not represent a valid dictionary.")
        
    except (ValueError, SyntaxError):
        print("Error: Unable to convert the string to a dictionary.")




def send_note():
    if min_val < (max_val/2):
        try:
            server = smtplib.AMTP(smtp_server, smtp_port)
            server.starttls()
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print('Email sent successfully!')
        except Exception as e:
            print('Email could not be sent. Error:', str(e))
