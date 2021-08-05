import requests
import json 
_headers = {
    "PRIVATE-TOKEN": "6-8l7GcRuvnz7xVLxiKv"
}
print('start')

r = requests.get('https://git.woa.com/api/v3/projects',headers=_headers)
print('11111111111111111111')
print('2')

r = r.json()
id = r[1]['id']
print(id)

name = r[1]['path_with_namespace']
print(name)

print('222222222222222222')
