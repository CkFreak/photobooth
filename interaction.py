import os
import time
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_address = "timbo@tributi.de"


def start_conversation():
    print("\033[H\033[J")
    print("Welcome to the Christophorus Photobooth! We are happy you are here!")

    response = raw_input("Do you want to take a picture? [yes, y, no, n]\n")
    return response


def countdown(n):
    print("Starting count-down!")
    print("Get Ready!")
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
        if n == 0:
            return


def take_picture():
    print("SMILE! :D\n")
    subprocess.call("./image.sh")
    print("Your image was captured!\n")


def get_email_addresses():
    print("Please enter your email to receive the image.")
    addresses = raw_input("More than one address is possible. Please separate them with ','\n")
    return addresses


def send_mail_to(address):
    print("Preparing image to be sent")
    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = address
    msg["Subject"] = "CH-Photobooth"

    body = "In the attachment you will find your personal image!\nThis is a unique picture it was deleted" \
           " from the photobooth for privacy reasons.\n\nWe hope you had a great time!" \
           "\nChristophorus Haus Semesterparty Team"
    msg.attach(MIMEText(body, "plain"))
    filename = "/home/pi/Documents/capture.jpg"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    print("Encoding image")
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    print("Establishing connection")
    server = smtplib.SMTP("mailout.tributi.de", 587)
    server.starttls()
    print("Logging in to Mail Server")
    server.login(os.environ["MAIL_USER"], os.environ["MAIL_PASSWORD"])
    text = msg.as_string()
    print("Sending mail...")
    server.sendmail(from_address, address, text)
    server.quit()
    print("Email was sent to %s" % address)
    os.remove(filename)
    print("The image was purged! You are the only one to ever receive it :)")
    print("Thank you for using our photobooth")
    print("Feedback can be sent to: blaesche.m@gmail.com\n")
