import os
import paramiko 
retValue = os.system('ssh admin@10.5.71.74')
ssh_client = paramiko.SSHClient()
ssh_client = retValue
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = '10.5.71.74', username ='admin', password = '')
print(ssh_client) 

stdin,stdout,stderr = ssh_client.exec_command('en')

print(stdout.readlines()) 
print('End')
