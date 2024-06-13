import json

data = '''
[
    {
        "name" : "Chuck",
        "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
        },
        "email" : {
        "hide" : "yes"
        }
    }
]
'''

info = json.loads(data)
for item in info:
    print('Name:', item['name'])
    print('Attr:', item['email'])