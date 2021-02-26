import requests
import bs4
import json
import re
import urllib
url2 = "https://www.bilibili.com/BV1LA41177bL"

url = 'https://www.bilibili.com/bangumi/play/ep341208'
headers1 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
#response = requests.get(url=url, timeout=30, headers=headers)

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "5d235d20-e656-4a23-800d-cd10fd065c1f"
}

response = requests.request("POST", url, headers=headers)

#str = '/(?<json>(?:\{\s*"(?:\\"|[^"])+"\s*:\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null)(?:\s*,\s*"(?:\\"|[^"])+"\s*:\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null))*\s*\}|\[\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null)(?:\s*,\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null))*\s*\]))/'

pattern=re.compile(r'"name": "(.*?)",')



#pattm=re.compile('(?<json>(?:\{\s*"(?:\\"|[^"])+"\s*:\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null)(?:\s*,\s*"(?:\\"|[^"])+"\s*:\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null))*\s*\}|\[\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null)(?:\s*,\s*(?:(?P>json)|"(?:\\"|[^"])+"|[-+]?(0|[1-9]\d*)(?:\.[-+]?(0|[1-9]\d*))?(?:[eE][-+]?(0|[1-9]\d*))?|(?:true|false)|null))*\s*\]))')

print(re.findall(pattern,response.text))

json1 = urllib.parse.unquote(response.text)


print()
print()
print()
print()

print(json1)
print(type(json1))
#print(response.text)




