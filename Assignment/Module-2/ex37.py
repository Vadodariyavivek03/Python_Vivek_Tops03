import requests

url = "https://fakestoreapi.com/products"

req = requests.get(url)
data = req.json()

for i in data:
    print(i["id"], i["title"])