#!/usr/bin/python
#import packages
import time
import logging
import smtplib
from datetime import datetime
from sense_hat import SenseHat

# COLOR TEST
sense = SenseHat()
r = 255
g = 255
b = 255
sense.clear((r, g, b))
time.sleep(1)
r = 255
g = 0
b = 0
sense.clear((r, g, b))
time.sleep(1)
r = 0
g = 255
b = 0
sense.clear((r, g, b))
time.sleep(1)
r = 0
g = 0
b = 255
sense.clear((r, g, b))
time.sleep(1)
r = 0
g = 0
b = 0
sense.clear((r, g, b))
#Humidity Reading

#Logging 
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
today = datetime.today()
date = today.strftime("%b-%d-%Y--%H-%M-%S")
handler = logging.FileHandler("enterloglocation here"+date+".log","w", "utf-8")
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
root_logger.addHandler(handler)
humidity = ('%.3f'% sense.humidity)
red=(255,0,0)
grey=(128,128,128)
sense.show_message(humidity, text_colour=red, back_colour=grey)
logging.debug("The humidity for the room was " + humidity )
sense.clear()

#Email Notification
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #Enter the email that you will be using to send here
GMAIL_PASSWORD = #Enter the password of the email that you will be using to send here

#Create class to send an email
class Emailer:
	def sendmail(self, recipient,  subject, content):
		#Creating the headers
		headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
			"To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
		headers = "\r\n".join(headers)

		#Connect to Gmail Server
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		session.ehlo()
		session.starttls()
		session.ehlo()

		#Login to Gmail
		session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

		#Send Email & Exit
		session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
		session.quit
sender = Emailer()

sendTo = #enter email recipient here
emailSubject = "IOT Research: Humidity In the lab " + date
emailContent = "This is the Pi in the lab.\n The humidity in the lab room is "+ humidity

#Sends an email to the "snedTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
sender.sendmail(sendTo, emailSubject, emailContent)
