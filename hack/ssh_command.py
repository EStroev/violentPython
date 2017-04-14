import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = 'ssh ' + user + '@' + host
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error Connection')
        return
    elif ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connection')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = '10.211.55.4'
    user = 'root'
    password = 'P@ssw0rd'

    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow')

if __name__ == '__main__':
    main()