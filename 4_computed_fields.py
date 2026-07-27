from pydantic import BaseModel, computed_field, EmailStr, AnyUrl, field_validator, fields
from typing import List, Dict, Annotated, AnyStr, Optional
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact:Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

def patient_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print("BMI", patient.calculate_bmi)
    print("Update")

info = {'name':'ssp','age':28,'weight':80,"height":1.77,"married":'No','allergies':['pollen','dust'],"contact":{"Email":"shubhamsaurav@gmail.com","Mobile No":"9122511545"}}

patient1=Patient(**info)
patient_info(patient1)
