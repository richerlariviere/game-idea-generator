import json
import random

with open('adj.json') as data_file:
    adj = json.load(data_file)

with open('gametypes.json') as data_file:
    gametypes = json.load(data_file)

with open('locations.json') as data_file:
    locations = json.load(data_file)

print("It's like " + random.choice(adj)['name'] + " " + random.choice(gametypes)['name'] + " game set in " + random.choice(locations)['name'])
