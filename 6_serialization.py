from pydantic import BaseModel
from typing import Dict, List

class Address(BaseModel):
    city:str
    state:str
    pincode:str


class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address

address_info = {"city":"durg","state":"chhattisgarh","pincode":"491002"}
address1=Address(**address_info)

patient_info = {'name':'ssp', "gender":'male',"age":29,"address":address1}
patient1 = Patient(**patient_info)
print(patient1.address)
print(patient1.address.pincode)

# ## Export your data  only in two type 1st Dict and Json

#Export in Dict
temp = patient1.model_dump(exclude="gender") ## you can use include, exclude and eclude_unset=True
print(temp)
# print(type(temp))


# #Export in Json                             you can use include, exclude and eclude_unset=True
temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp))