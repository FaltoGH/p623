import requests
res=requests.post("http://127.0.0.1:10015/greet",data={"username":"ec2-user2"})
print(res.status_code)
print(res.headers)
print(res.text)
