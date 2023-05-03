import subprocess
import smtplib
import time
import platform

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
config.readline()
config.readline()
process_name = config.readline()[13:-1]

# Set up the email message
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_password = app_password
recipient_email = target_email
subject = "Server process is down"
body = "The server process is not running. Please check the server."

# Set up the process to monitor
messaged = False
# Loop continuously to monitor the process
while True:
    # Check if the process is running
    process_running = False
    if platform.system() == "Windows":
        try:
            output = subprocess.check_output("tasklist")
            if process_name in str(output):
                process_running = True
        except subprocess.CalledProcessError:
            pass
    else:
        try:
            output = subprocess.check_output(["ps", "aux"])
            for line in output.splitlines():
                if process_name.encode() in line:
                    process_running = True
                    break
        except subprocess.CalledProcessError:
            pass

    # If the process is not running, send an email
    if not process_running and not messaged:
        messaged = True
        print("server outage detected")
        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.encode())
    elif(process_running):
        messaged = False    
    # Wait for some time before checking again
    time.sleep(polling_interval)

