import requests

# status='available'
# res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
#                     headers = {'accept': 'application/json'})
# print(res.text)
# print(res.status_code)
# print(res.json())
# print (type(res.json()))

url = 'https://petstore.swagger.io/v2/pet'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
print(response.text)
print (type(response.json()))

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.text)
print(res.status_code)
print(res.json())
print (type(res.json()))

data2={
  "id": 9223372036854257000,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res2 = requests.put(url, headers=headers, json=data2)

print(res2.status_code)
print(res2.json())
print (type(res2.json()))

res2 = requests.delete( f"https://petstore.swagger.io/v2/pet/9223372036854257000", headers=headers, json=data2)

print(res2.status_code)