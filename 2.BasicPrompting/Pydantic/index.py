from pydantic import BaseModel,EmailStr,Field,field_validator

class User(BaseModel):
    id:int = Field(gt=0,description="Id of the employee, should be gt 0")
    name:str = Field(min_length=3,description="user name, min 3 characters")
    username:str = Field(alias="userName")
    age:int=Field(gt=0,lt=90,description="The user age")
    email:EmailStr
    is_active:bool = True

    @field_validator("username")
    @classmethod
    def validate_username_must_be_alphanumeric(cls,v:str)->str:
        if not v.isalnum():
            raise ValueError("The username must be alphanumeric")
        
        if not any(char.isalpha() for char in v):
            raise ValueError("Username must contain at least one letter")

        if not any(char.isdigit() for char in v):
            raise ValueError("Username must contain at least one number")

        return v.lower()

user =User(
    id=1,
    name="Anurag",
    userName="Anurag11",
    age=51,
    email="anurag@dsgroup.com",
    # is_active=True,
)
raw_data = {
    "id":"2",
    "name":"Anu",
    "userName":"Anu21",
    "age":25,
    "email":"anu@dsgroup.com",
    "is_active":False
}
print(user)
user1 = User.model_validate(raw_data)
print(user1.model_dump_json(by_alias=True))