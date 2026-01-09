from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Bengaluru', 
                'state': 'Karnataka', 
                'pin': '560097'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Amith Kumar', 
                'gender': 'male', 
                'age': 25, 
                'address': address1}
patient1 = Patient(**patient_dict)

print(patient1.name)
print(patient1.address.city)

# serialization
temp = patient1.model_dump()
print(temp)
print(type(temp))

temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2))

# excluding a field
temp3 = patient1.model_dump(exclude=['age'])
print(temp3)