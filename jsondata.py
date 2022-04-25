import json


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


InvalidJsonData = """{"company":{"employee": {"name":"emma","payable":{"salary":7000,
"bonus":800}}}}"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)

sample = """[
    {
        "id": 1,
        "name": "name1",
        "color": ["red", "green"]
        
    },
    {
        "id": 2, 
        "name":"name2",
        "color":[
            "pink",
            "yellow"
        ]
    }
]"""

data = []
try:
    data = json.loads(sample)
except Exception as e:
    print(e)

dataList = [item.get('id') for item in data]
print(dataList, " is True")
