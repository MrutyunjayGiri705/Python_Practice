import json
data = {"name": "Alice", "age": 25, "city": "New York"}
# # json_string=json.dumps(data)
# # print(json_string)
# # print(type(json_string))
# with open("data.json","w") as file:
#     json.dump(data,file)
    
 
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
 
# python_obj = json.loads(json_data)
# print(python_obj) 
# print(type(python_obj)) 
# with open("data.json", "r") as file:
#     python_data = json.load(file)
#     print(python_data)
formatted_json = json.dumps(data, indent=4)
print(formatted_json,type(formatted_json))