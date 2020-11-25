import paramiko


cmd = "ls /home/dichen/data"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

usr = "super_root"
passwd = "real_password"
host = "tom.crazy.com"

ssh.connect(host, 22, usr, passwd)

stdin, stdout, stderr = ssh.exec_command(cmd)

lines = stdout.readlines()

print(lines)
