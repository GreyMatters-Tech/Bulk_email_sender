#impoet the necessary modules
import smtplib, ssl, csv
from email.message import EmailMessage

sender = '' #add your sender email address
password = '' #add your app password

subject = '' #add the subject #add the subject to your email
body_message = '' #type the message you want to send

#connect to our outgoing mail SMTP server
context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context)

server.login(sender, password)

#The formula we will use to send emails
with open('csv file path', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = subject
        em.set_content(body_message)
        server.send_message(em)
        print("The message sent")

server.close()
print("Done @GreyMatter_Bots")
