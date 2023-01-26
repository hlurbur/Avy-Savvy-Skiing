"""
emailer.py sends an email containing the avalanche forecast and suggested routes
to ski from AvyScraper@gmail.com using the smtplib library.
MIMEText and MIMEMultipart are used to format the email text and subject. 
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from analyzeRoutes import *

#email the messages are sent from and app password. Used to get around two-step
#verification when the program logs into the account.
sender_email = "AvyScraper@gmail.com"
app_password = "" #enter password here 


def sendEmail(recipient, name, routeSuggestion, forecastLink):
    """
    Sends an email to a user with the suggested routes for them to ski
    
    Args:
    recipient: the email address of the user that will receive the email
    name: the string name of the user
    routeSuggestion: the string route suggestion for the user to ski
    forecastLink: the link to the forecast of the users preferred region
    
    """


    message = MIMEMultipart()
    message["Subject"] = "Ski Recommendation for: {}".format(name)
    message["From"] = sender_email
    message["To"] = recipient
    intro = "Howdy " + name + "!"
    middle = "Your route suggestions for today are:"
    beacon = "Don't forget your beacon probe and shovel!"
    goodbye = "-The Snow Gods"
    suggestion = "" 
    # Create suggestion string based on the suggestion of the day
    if routeSuggestion == "There are no safe routes to ski today:(":
        suggestion += routeSuggestion
    else:
        for route in routeSuggestion:
            suggestion += str(route)+ "\n"
    
    #Link the forecast to the desired region
    forecastMsg = "View the full forecast for the day at the link below :)"
    link = forecastLink
    msg = intro + "\n" + middle + "\n" + suggestion + forecastMsg + "\n" + link + "\n" + beacon + "\n" + goodbye

    message.attach(MIMEText(msg, 'plain'))
    
    text = message.as_string()

    
    #create a secure SSL connection
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender_email, app_password)
    s.sendmail(sender_email, recipient, text)
    s.quit()

