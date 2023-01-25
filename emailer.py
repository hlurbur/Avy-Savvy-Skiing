import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from analyzeRoutes import *

sender_email = "AvyScraper@gmail.com"
gmail_password = "vusezjvbwbnkpold"


def sendEmail(recipient, name, routeSuggestion):
    """
    Sends an email to a user with the suggested routes for them to ski
    
    Args:
    recipient: the email address of the user that will recieve the email
    name: the strint name of the user
    routeSuggestion: the string route suggestion for the user to ski
    
    """


    message = MIMEMultipart()
    message["Subject"] = "Ski Recommendation for: {}".format(name)
    message["From"] = sender_email
    message["To"] = recipient
    intro = "Howdy " + name + "!"
    middle = "Your route suggestions for today are:"
    beacon = "Don't forget your beacon probe and shovel!"
    goodbye = "-The Snow Gods"
    msg = intro + "\n" + middle + "\n" + routeSuggestion + "\n" + beacon + "\n" + goodbye

    message.attach(MIMEText(msg, 'plain'))
    
    text = message.as_string()

    
    #create a secure SSL connection
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender_email, gmail_password)
    s.sendmail(sender_email, recipient, text)
    s.quit()

