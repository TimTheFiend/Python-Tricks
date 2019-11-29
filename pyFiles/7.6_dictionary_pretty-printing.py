import json

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(mapping, indent=4, sort_keys=True))
"""Output: 
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
"""