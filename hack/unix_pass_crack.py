import crypt


def test_pass(crypto_pass):
    salt = crypto_pass[0:2]
    with open('dictionary.txt', 'r') as dictionary:
        for word in dictionary.readlines():
            word = word.strip('\n')
            crypto_word = crypt.crypt(word, salt)
            if crypto_pass == crypto_word:
                print('[+] Found password: %s' % word)
                return
    print('[-] Password not found')
    return


def main():
    with open('passwords.txt', 'r') as pass_file:
        for line in pass_file.readlines():
            if ':' in line:
                user = line.split(':')[0]
                password = line.split(':')[1].strip(' ')
                print(user, password)
                print('Cracking password for %s...' % user)
                test_pass(password)

if __name__ == '__main__':
    main()


