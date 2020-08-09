# JSON (JavaScript Object Notation) module

# JSON encoder and decoder
# https://docs.python.org/3/library/json.html


# create json
# json.dump
# json.dumps
import json

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], indent=2))
# '["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
# "\"foo\bar"
print(json.dumps('\u1234'))
# "\u1234"
print(json.dumps('\\'))
# "\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
# {"a": 0, "b": 0, "c": 0}
from io import StringIO

io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
# '["streaming API"]'
############################################
# decode json
# json.load
# json.loads
jsonx = """{
    "name": "Python",
    "platform": [
        "Linux",
        "Windows",
        "MacOS"
    ]
}
"""

data = StringIO()
print(json.loads(jsonx))
# {'name': 'Python', 'platform': ['Linux', 'Windows', 'MacOS']}


print(json.loads(jsonx, object_hook=list))
# ['name', 'platform']

print(json.loads(jsonx, object_pairs_hook=str))
# [('name', 'Python'), ('platform', ['Linux', 'Windows', 'MacOS'])]

