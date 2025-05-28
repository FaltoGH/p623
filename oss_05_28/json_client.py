import requests

res=requests.get("http://127.0.0.1:10015/api/hello")
print(res.status_code)
print(res.json())

payload={"name":"soobum", "age":21}
res2=requests.post("http://127.0.0.1:10015/api/echo",json=payload)
print(res2.status_code)
print(res2.json())
