import json

variables = open('utils/variables.json')
json_load = json.loads(variables.read())

Authorization = json_load['Authorization']
Endpoint =json_load['Endpoint']
