import paramiko
username="root"
password="root@123"
ip="192.168.40.17"
port=22
command = "ls"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, port=port, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command(command)
lines=stdout.readlines()
print(lines)
import smtplib
gmail_user = 'gattupalliraviteja007@gmail.com'
gmail_password = 'fgjmjllortq1'

sent_from = "CLOUD4C"
to = ['sahithi.kolli@cloud4c.com']
subject = "ALERT AUTOMATIC MAIL"
body = lines

email_text = """From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print ('Email sent!')
except:
    print ('Something went wrong...')

