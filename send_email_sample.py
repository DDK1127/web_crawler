from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from string import Template
import smtplib
import glob

content = MIMEMultipart()  
content["subject"] = "This is a test email"  # mail title
content["from"] = ""  # sender
content["to"] = "" # receiver
googlepassword = ""


template = Template(open("send_email_template.html").read())  # read html file
body = template.substitute({ "user": "D" })
content.attach(MIMEText(body, "html"))  

# Open the image file in bynary mode
image_files = glob.glob('')
for image_file in image_files:
    with open(image_file, 'rb') as img:
        mime_img = MIMEImage(img.read(), _subtype="jpg")
    content.attach(mime_img)

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp: 
    try:
        smtp.ehlo()  # verify connection
        smtp.starttls()  # encrypting
        smtp.login("", googlepassword)  # sender email login
        smtp.send_message(content) 
        print("Successfully sent email!")
    except Exception as e:
        print("Error message: ", e)