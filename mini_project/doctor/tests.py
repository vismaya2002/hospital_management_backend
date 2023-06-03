import requests
import json
id=input("enter the doctorid: ")
response_API = requests.get('http://127.0.0.1:8000/doctor/api/'+id)
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
department,doctorname,doctorid = parse_json['department'],parse_json['doctorname'],parse_json['doctorid']
print("the name of the doctor with id ",doctorid," is ",doctorname," in the department ",department)

