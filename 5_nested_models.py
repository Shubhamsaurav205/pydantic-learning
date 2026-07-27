from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address

address_dict = {"city":"Durg","state":"chhattisgarh","pincode":"491002"}
address1 = Address(**address_dict)

paitent_dicxt = {"name":"ssp","gender":"male",'age':27,"address":address1}
Patient1 = Patient(**paitent_dicxt)

print(Patient1)
print(Patient1.name)
print(Patient1.address)
print(Patient1.address.city)
print(Patient1.address.state)
print(Patient1.address.pincode)