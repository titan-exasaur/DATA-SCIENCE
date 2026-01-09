from typing import List, Dict
from pydantic import BaseModel, EmailStr
from pydantic import field_validator

class Patient(BaseModel):
    # Data type validation schema
    # name: str = Field(min_length=1, max_length=50)
    name: str
    email: EmailStr
    age: int
    weight: float
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com'] 
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f'Invalid email domain {domain_name}')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after') # mode='before' is default and if before validation runs before data is converted
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError(f'Invalid age {value}')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data updated successfully')

patient_info = {'name': 'kumar', 
                'email': 'l6u0B@hdfc.com',
                'linkedin_url': 'https://www.linkedin.com/in/kumar',
                'age': '20',
                'weight': 87,
                'allergies': ['lactose'],
                'contact_details': {'email': 'l6u0B@example.com',
                                     'phone': '1234567890'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)