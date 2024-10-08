import requests
res = requests.get('http://116.198.235.112:8001/docs#/').text
print(res)
