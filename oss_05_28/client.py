import requests
res=requests.get("http://127.0.0.1:10015")
print(res.status_code)
print(res.headers)
print(res.text)
