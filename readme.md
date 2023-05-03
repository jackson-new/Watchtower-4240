# Watchtower

Watchtower is a Python-based server monitoring tool that can notify you via email when your server goes down. It consists of two programs: the local monitor, which watches for a specific process name using the `ps aux` command, and the foreign monitor, which uses pings to see if it can reach a server.

## Getting Started

### Prerequisites

Before you can use Watchtower, you need to make sure that the following dependencies are installed on your server:

- secure-smtplib
- subprocess.run

You can install these dependencies using pip3:

```
pip3 install smtplib
pip3 install subprocess
```

### Installing

To install Watchtower, simply clone this repository to your machine:

```
git clone https://github.com/jackson-new/Watchtower-4240.git
```

### Configuring

Before you can use Watchtower, you need to configure it by editing the `config.txt` file. Here's an example configuration file:

```
  # Email that will be notified of downtime
target_email=target@gmail.com
  # Email that will send the email notifications
sender_email=sender@gmail.com
  # App password for sender_email (Not regular password. Must be configured as an app password through gmail settings)
app_password=abcdefghijklmnop
  # Amount of time in between checks to see if the server is down in seconds
polling_interval=5
# IP of server to be monitored. Only needed for foreign_monitor.py
server_ip=10.9.0.5
  # Proccess name of the server. Only needed for local_monitor.py
process_name=python3 flask_server.py
```

You should replace `target@gmail.com` with the email address that you want to receive notifications, and `sender@gmail.com` with the email address that you want to use to send notifications. You should also replace `abcdefghijklmnop` with the app password that you generated for your Gmail account.

If you're using the local monitor, you should replace `python3 flask_server.py` with the process name of the server that you want to monitor.

### Running

To run Watchtower, simply run the following command:

```
python3 local_monitor.py
```

or

```
python3 foreign_monitor.py
```

This will start the Watchtower application, which will monitor your server and send email notifications when it goes down.
