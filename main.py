import requests

url = "http://numbersapi.com/"
res = requests.get(url + "43" + "/trivia")
print(res.status_code)
print(res.text)