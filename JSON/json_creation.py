import json
student_data=[{"student":"student1","marks":10,"status":"Fail"},
{"student":"student2","marks":20,"status":"Fail"},
{"student":"student3","marks":30,"status":"Fail"},
{"student":"student4","marks":40,"status":"Fail"},
{"student":"student5","marks":50,"status":"pass"},
{"student":"student6","marks":60,"status":"pass"},
]
with open("student_json_detail.json", "w") as studs:
    json.dump(student_data,studs)
print("JSON created")