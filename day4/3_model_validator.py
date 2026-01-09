from typing import List, Dict
from pydantic import BaseModel, EmailStr
from pydantic import model_validator

class Patient(BaseModel):
    # Data type validation schema
    # name: str = Field(min_length=1, max_length=50)
    name: str
    email: EmailStr
    age: int
    weight: float
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for elderly patients')
        return model
    


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
                'age': '60',
                'weight': 87,
                'allergies': ['lactose'],
                'contact_details': {'email': 'l6u0B@example.com',
                                     'phone': '1234567890'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)