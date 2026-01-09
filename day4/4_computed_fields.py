from typing import List, Dict
from pydantic import BaseModel, EmailStr
from pydantic import computed_field

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.calculate_bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print('Data updated successfully')

patient_info = {'name': 'kumar', 
                'email': 'l6u0B@hdfc.com',
                'linkedin_url': 'https://www.linkedin.com/in/kumar',
                'age': '60',
                'weight': 87,
                'height': 1.78,
                'allergies': ['lactose'],
                'contact_details': {'email': 'l6u0B@example.com',
                                     'phone': '1234567890'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)