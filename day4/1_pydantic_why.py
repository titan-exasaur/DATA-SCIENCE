from typing import List, Dict, Optional
from pydantic import BaseModel # Pydantic is a data validation library
from pydantic import EmailStr # takes email as input
from pydantic import AnyUrl # takes url as input
from pydantic import Field # used to set constraints e.g., min_length, gt, ge etc
from typing import Annotated # used to write descriptions

class Patient(BaseModel):
    # Data type validation schema
    # name: str = Field(min_length=1, max_length=50)
    name: Annotated[str, Field(min_length=1, max_length=50,
                    title='Name of the patient',
                    description='Write name of the patient in less than 50 characters',
                    examples=['akash', 'kumar'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)] # strict = True means that the value must be greater than 0 and stictly float
    married: bool
    allergies: List[str] = Field(max_length=5)
    contact_details: Dict[str, str]

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Data inserted successfully')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data updated successfully')

patient_info = {'name': 'kumar', 
                'email': 'l6u0B@example.com',
                'linkedin_url': 'https://www.linkedin.com/in/kumar',
                'age': 20,
                'weight': 87,
                'married': False,
                'allergies': ['lactose'],
                'contact_details': {'email': 'l6u0B@example.com',
                                     'phone': '1234567890'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)