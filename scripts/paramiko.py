
from paramiko import SSHClient

client = SSHClient()
client.connect("192.168.0.135", username='dichen', password='CDstc9616', look_for_keys=False)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

stdin, stdout, stderr = client.exec_command("ls /home/dichen")
