# it allows you to define your own validation rules that go beyond built-in constraints like
# For example:

# Name should not contain numbers.
# Age should be an even number.
# Email should belong to a specific company.
# Password should contain a special character.


#Logic of code base on this "Email should belong to a specific company"

from pydantic import BaseModel, EmailStr, field_validator, fields
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies: Optional[List[str]] =None
    email:EmailStr
    contact_details:dict[str,str]


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        vaild_domain = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in vaild_domain:
            raise ValueError('Not a vaild domain')
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()





def upadate_patient_info(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact_details)


info = {"name":'ssp',"age":26,"weight":80.1,"married":True,"email":'shubham@hdfc.com',"contact_details":{"mobile_no":"9122511545"}}
patient1 = Patient(**info)
upadate_patient_info(patient1)
