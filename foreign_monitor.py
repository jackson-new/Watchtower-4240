import os
import smtplib
import time

# Read configuration data from file
config = open("./config.txt", "r")

config.readline()
target_email = config.readline()[13:]

config.readline()
sender_email = config.readline()[13:]

config.readline()
app_password = config.readline()[13:]

config.readline()
polling_interval = int(config.readline()[17:])

config.readline()
server = config.readline()[10:]

# set the hostname or IP address of the server you want to monitor
smtp_server_address = "smtp.gmail.com"
smtp_port = 587
# set the email address to send alerts to
to_email = target_email

# set the time interval to check the server status (in seconds)
interval = polling_interval
messaged = False

while True:
    response = os.system("ping -c 1 " + server)

    # server is down, send an email alert
    if response != 0 and not messaged:
        messaged = True
        print(f"{server} is down!")
        subject = f"{server} is down!"
        body = f"{server} is not responding."
        message = f"Subject: {subject}\n\n{body}"
        smtp_server = smtplib.SMTP(smtp_server_address, smtp_port)
        smtp_server.starttls()
        smtp_server.login(sender_email, app_password)
        smtp_server.sendmail(sender_email, to_email, message)
        smtp_server.quit()
    elif(response == 0):
        messaged = False

    # wait for the specified interval before checking again
    time.sleep(interval)
