#Model_vaildator 
#A model validator is used to validate the entire model, rather than a single field.

#In simple words: field_validator validates one field, while model_validator validates multiple fields together
#Eg -  Password Comformation 

from pydantic import BaseModel, model_validator

class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def check_password(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

User(
    password="abc123",
    confirm_password="abc12"
)