import json
import paramiko
import pandas 
import smtplib
##taking two alerts
 
s='''[{"host": "FIS_Suryoday_WIN_WSUYDCDBBUR01_10.51.33.41",
"hostid": 11115,
"ip": "192.168.40.17",
"issue_description": "FIS_SURYODAY_BureauOne_WSUYDCDBBUR01_192.168.40.17_DC_WIN - High - CPU Utilization is 88.14 %",
"itemid": 57098,
"objectid": 39214,
"port": "10050",
"priority": "High",
"proxy": "FIS_Suryoday_Proxy",
"proxyid": 10155},
{
 
"host": "FIS_ESAF_WIN_10.61.65.46",
"hostid": 10661,
"ip": "10.61.65.46",
"issue_description": "FIS_ESAF_Servosys_WESFDCABAPP01_10.61.65.46_DC_WIN - Information - Zabbix agent Unreachable",
"itemid": 39989,
"objectid": 26040,
"port": "10050",
"priority": "Average",
"proxy": "FIS_ESAF_Proxy",
"proxyid": 10149
 
 
}]
'''
jf=json.loads(s)
jan= pandas.read_excel('ravi.xlsx', sheet_name='Sheet2')
ip=jan["ip"]
host=jan["host"]
k={}
for i in range(0,len(ip)):
    k.update({ip[i]:host[i]})
def platform(ip):
    s=""
    if not ip in k.keys():
        return "NA"
    hs=k[ip]
    ip=ip.split(".")
    dup=["41","51","61","71","81","91","168"]
    if ip[1] in dup:
        s=s+"DC"
    else:
        s=s+"DR"
    if hs[0]=="W":
        s=s+" WIN"
    else:
        s=s+" LIN"
    return s
 
print(platform("192.168.40.17"))
for i in jf:
    print(i["ip"])
    print(i["issue_description"])
    desc=platform(i["ip"])
    dcpu=i["issue_description"]
    if desc!="NA":
        if "CPU" in dcpu or "Load" in dcpu:
            #####excute server cod
                #import paramiko
                username="root"
                password="root@123"
                ip="192.168.40.17"
                port=22
                command = "ls"
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=ip, port=port, username=username, password=password)
                stdin, stdout, stderr = ssh.exec_command(command)
                output=stdout.readlines()
                #print(output)
		l=output
		s=""
		for i in l:
    			s=s+i[2:-1]
    			s=s+"\n"
		print(s)
gmail_user = 'gattupalliraviteja007@gmail.com'
gmail_password = 'fgjmjllortq1'
sent_from = "CLOUD4C"
to = ['sahithi.kolli@cloud4c.com']
subject = jf[0]["issue_description"]
body = s
 
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
