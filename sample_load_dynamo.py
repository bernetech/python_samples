#!/opt/local/bin/python

## put the "cars" sample json file into dynamo db after creating the table
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('autos')

print(table.creation_date_time)

# read the json file
with open('../cars.json') as json_data:
    items = json.load(json_data)

    with table.batch_writer() as batch:
        ## loop through the json objects - each value in the manufacturer key
        ## is a list, so convert it to a dict before pushing 
        for item in items['manufacturer']:
            batch.put_item(Item=dict(item))

## input ('../cars.json' referenced above):
#{
#	"info": {
#		"generated_on": "2022-08-09  19:25:34",
#		"version": "v1"
#	},
#	"manufacturer": [
#		{
#			"name": "Audi",
#			"id":	1,
#			"num_features": 2,
#			"features": [
#				{
#						"featurename": "seat heaters",
#						"standard": "N",
#						"cost": 100
#				},
#				{
#						"featurename": "A/C",
#						"standard": "Y",
#						"cost": 0
#				}
#			]
#		},
#		{
#			"name": "BMW",
#			"id": 2,
#			"num_features": 3,
#			"features": [
#				{
#						"featurename": "seat heaters",
#						"standard": "Y",
#						"cost": 0
#				},
#				{
#						"featurename": "backup camera",
#						"standard": "N",
#						"cost": 500
#				},
#				{
#						"featurename": "A/C",
#						"standard": "Y",
#						"cost": 0
#				}
#			]
#		}
#	]
#}
