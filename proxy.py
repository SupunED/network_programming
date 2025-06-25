import requests

proxies = {
    'https': 'https://185.159.153.234:80'
}

response = requests.get("http://ipinfo.io/json", proxies=proxies)

print(response.json()['country'])
print(response.json()['region'])
print(response.text)