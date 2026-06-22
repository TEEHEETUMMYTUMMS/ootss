import json
import os

j = json.load(open('../data/markers.json'))

names = open('order.txt').read().splitlines()

name_order = {name: index for index, name in enumerate(names)}

# Sort features by the order of names
features = sorted(
    j['features'],
    key=lambda feature: name_order.get(feature.get('properties', {}).get('name'), len(names))
)

out = {"type": "FeatureCollection", "features": features}

f = open('markers.json', 'w', encoding='utf-8', newline='\n')
json.dump(out, f, indent=2)




