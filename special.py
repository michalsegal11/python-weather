import requests
import random
import json
import string


base_url="https://gorest.co.in"
headers = {
    "Authorization": "Bearer f410a6f94046632ec880ffcb85bbc4e158b77b0577c96e7c5918d88f60988694"
}


#Get
def get_request():
    url=base_url+"/public/v2/users"
    response=requests.get(url,headers=headers)
    assert response.status_code==200

    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json response body: ",json_data)
    print("str response body: ",json_str)



#Post
def post_request():
    url=base_url+"/public/v2/users"
    data = {
    "name": "Michal",
    "email": "michal@example.com",
    "gender": "female",
    "status": "active"
}
    response=requests.post(url,headers=headers,json=data)
    json_data=response.json()
    assert response.status_code==201
    json_str=json.dumps(json_data,indent=4)
    print("json response body: ",json_data)
    print("str response body: ",json_str)
    user_id=json_data["id"]
    assert "name" in json_data
    assert json_data["name"]=="Michal"
    return user_id



#Put
def put_request(id1):
    url=base_url+f"/public/v2/users/{id1}"
    data = {
    "name": "Michal11",
    "email": "michal@example.com",
    "gender": "female",
    "status": "active"
}
    response=requests.put(url,headers=headers,json=data)
    json_data=response.json()
    assert response.status_code==200
    json_str=json.dumps(json_data,indent=4)
    print("json response body: ",json_data)
    print("str response body: ",json_str)
    assert json_data["id"]==id1
    assert json_data["name"]=="Michal11" 
  
#Delete
def delete_request(id1):
    url=base_url+f"/public/v2/users/{id1}"
    response=requests.delete(url,headers=headers)
    assert response.status_code==204
    print("...........DELETE USER IS DONE..............")

get_request()
put_request(7958455)
delete_request(7958455)
