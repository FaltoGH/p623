import requests
res=requests.get("http://127.0.0.1:10015/greet?username=ec2-user")
print(res.status_code)
print(res.headers)
print(res.text)
