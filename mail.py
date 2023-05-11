'''
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sender_email_id", "sender_email_id_password")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("sender_email_id", "receiver_email_id", message)

# terminating the session
s.quit()

'''

'''
import smtplib    
sender_mail = 'sender@fromdomain.com'    
receivers_mail = ['reciever@todomain.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")    
'''


'''

import smtplib    
sender_mail = 'sender@gmail.com'    
receivers_mail = ['reciever@gmail.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
   password = input('Enter the password');    
   smtpObj = smtplib.SMTP('gmail.com',587)    
   smtpobj.login(sender_mail,password)    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")
   '''


'''
import smtplib#simple mail transfer protocol
server=smtplib.SMTP("gmail.com",587)
server.starttls()
server.login("kesanabhavanee@gmail.com","1Bha2va3nee@")
server.sendmail("kesanabhavanee@gmail.com","kesanabhavanee@gmail.com","hello")
server.quit()
print("mail sent")
'''


'''

import smtplib
smtpObj=smtplib.SMTP('smtp.gmail.com',587)
#print(type(smtObj))
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("kesanabhavanee@gmail.com","1Bha2va3nee@")
message='Subject:So long.\nDear shortyy, so long and thanks for all the fish. Sincerely, pottii'
smtpObj.sendmail("kesanabhavanee@gmail.com","isrsvinay445@gmail.com",message)
smtpObj.quit()
print("sent")


'''


import smtplib
myemail="kesanabhavanee@gmail.com"
mypassword="1Bha2va3nee@"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=myemail,password=mypassword)
connection.sendmail(from_addr=myemail,tp_addr="isrsv455@gmail.com",msh="subscribe")
connection.close()


























