# pyhton script to get json array as input and sort it using age and name
# input file NAME file.json and make sure it is in the same directory
import json
from pprint import pprint
from collections import defaultdict
import operator

# validating the json
#schema = {
#    "properties" : {
#        "name" : {"type" : "string"},
#        "city" : {"type" : "string"},
#        "age" : {"type" : "number"},
#    }
#}

# assuming the data is accurate
file = open("file.json", "r")
data = json.load(file)

file.close()

list = []

for i in data['Persons']:
    #validate(i, schema)
    list.append(i)
    

print("Displaying the List sorted by name : ")
list.sort(key=operator.itemgetter('Name'))

for elm in list:
    print(elm)

print("Displaying the List sorted by age : ")
list.sort(key=operator.itemgetter('Age'))

for elm in list:
    print(elm)