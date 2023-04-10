import requests

url = 'http://www.wsb.com/Homework3/case02.php'
response = requests.get(url, allow_redirects=False)

flag = response.text.split('The flag is ')[1].split('</div>')[0]
print(flag)
