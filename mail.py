import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("emailhere", "passwordhere")

message = input("Type your message here: ")
receiver = input("Enter the receiver here: ")
for i in range(0,100):
    server.sendmail("sendersemailhere", receiver, message)
server.quit()
