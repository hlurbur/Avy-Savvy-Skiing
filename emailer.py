import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_user = "AvyScraper@gmail.com"
gmail_password = "vusezjvbwbnkpold"

#create a secure SSL connection
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(gmail_user, gmail_password)
s.sendmail(gmail_user, "mlurbur@gmail.com", "")
s.quit()