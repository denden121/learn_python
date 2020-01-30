import os
import tempfile
import json
import argparse

STORAGE = os.path.join(tempfile.gettempdir(), 'storage.data')

def get_value(key):
    data = get_data()
    if data.get(key):
        return data.get(key)
    else:
        return {}


def add(key,value):
    data = get_data()
    if data.get(key):
        data.get(key).append(value)
    else:
        data[key]=[value]
    with open(STORAGE,'w') as f:
        json.dump(data,f)


def get_data():
    if os.path.isfile(STORAGE):
        with open(STORAGE) as f:
            return json.loads(f.read())
    else:
        return {}

parser = argparse.ArgumentParser()  
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

if args.val:
    add(args.key,args.val)
else:
    print (", ".join(get_value(args.key)))