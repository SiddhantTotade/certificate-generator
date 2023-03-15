import smtplib
import ssl

sender = "mseitevents@matsuniversity.ac.in"
password = "Mats@2023"
receiver = "siddhanttotade.1994@gmail.com"
string = "Hello"
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, string)
