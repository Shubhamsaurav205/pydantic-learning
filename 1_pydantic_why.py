## Pydantic allow  for Data Vaildation and Type Vaildation 
 ##=========================================================Chapter- 1 Type Validation==========================================

from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

def pateint_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("Updated Sucessfully")

info = {"name":'shubham',"age":24}
patient1 = Patient(**info)
pateint_info(patient1)

# #Example 2
# # use of Dict, List

from typing import List, Dict
class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

def upadate_patient_info(patien:Patient):
    print(patien.name)
    print(patien.weight)
    print(patien.allergies)
    print(patien.contact_details)

info = {"name":'ssp',"age":26,"weight":80.1,"married":True,"allergies":["dust","pollen"], "contact_details":{"email":'shubham@gmail.com',"mobile_no":"9122511545"}}

patient1 =Patient(**info)
upadate_patient_info(patient1)


#Exmaple 3
#Use of Optional 

from pydantic import BaseModel
from typing import Dict, List, Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies: Optional[List[str]]=None
    contact_details:dict[str,str]

def upadate_patient_info(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)


info = {"name":'ssp',"age":26,"weight":80.1,"married":True, "contact_details":{"email":'shubham@gmail.com',"mobile_no":"9122511545"}}
patient1 = Patient(**info)
upadate_patient_info(patient1)

##==========================================================Chapter- 2 Data Validation =======================================================
#Example 1
# Use of EmailStr 

from pydantic import BaseModel, EmailStr
from typing import Dict, List, Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies: Optional[List[str]]=None
    email:EmailStr
    contact_details:dict[str,str]

def upadate_patient_info(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.allergies)
    print(patient.email)
    print(patient.contact_details)


info = {"name":'ssp',"age":26,"weight":80.1,"married":True,"email":'shubham@gmail.com',"contact_details":{"mobile_no":"9122511545"}}
patient1 = Patient(**info)
upadate_patient_info(patient1)

#Example 1
#use of AnyUral
from pydantic import BaseModel, EmailStr, AnyUrl
from typing import Dict, List, Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool
    allergies: Optional[List[str]]=None
    email:EmailStr
    linkedin_url:AnyUrl
    contact_details:dict[str,str]

def upadate_patient_info(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.allergies)
    print(patient.linkedin_url)
    print(patient.contact_details)


info = {"name":'ssp',"age":26,"weight":80.1,"married":True,"email":'shubham@gmail.com',"linkedin_url":"https://www.linkedin.com/in/shubham-saurav-pathak-02b958219/","contact_details":{"mobile_no":"9122511545"}}
patient1 = Patient(**info)
upadate_patient_info(patient1)


#Example 1
#Use of 'Field' it provide custom data vaildation and its also alloow to attache meta data eg. if add expamle of write name  here "SSP", "Saurav"
#(i)  suppose  age should be not gt =0, lt = 60 (age:int = Field(ge=0 lt =60))

#(ii) name: Annotated[str,field(max_length =50, tittle = "Name of the Patient", description = "Give the name of the patient in less than 50 chars", example = ["amit","saurav"])]

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Dict, List, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50,tittle = "Write name of patient",description="Give the name of the patient less than 50 characters", examples=['SSp','Saurav'])]
    age:int= Field(gt=0,lt=40)
    weight:float =Field(gt=0, lt=100,strict=True)## strict=float means strictly require only float value not string 
    married:Annotated[bool,Field(default=None, description="is the patient married or not ")]
    allergies: Optional[List[str]]=Field(default=None,max_length=5)
    email:EmailStr
    linkedin_url:AnyUrl
    contact_details:dict[str,str]

def upadate_patient_info(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.allergies)
    print(patient.linkedin_url)
    print(patient.contact_details)


info = {"name":'ssp',"age":26,"weight":80,"married":True,"email":'shubham@gmail.com',"linkedin_url":"https://www.linkedin.com/in/shubham-saurav-pathak-02b958219/","contact_details":{"mobile_no":"9122511545"}}
patient1 = Patient(**info)
upadate_patient_info(patient1)