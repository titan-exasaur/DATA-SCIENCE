import json
from pydantic import computed_field
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Path, HTTPException, Query

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", examples=['P001'])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient")]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2))
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
        
def load_data():
    with open("../data/patients.json", "r") as file:
        data = json.load(file)
    
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records"}

@app.get('/view')
def view():
    data = load_data()
    return data


def load_data():
    with open('../data/patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("../data/patients.json", "w") as f:
        json.dump(data, f)


@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., 
                                        description = "patient ID",
                                        example = "P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient ID not found"}


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = 'sort by height, weight or bmi'),
                order:str = Query('asc or desc'), description = 'sort in asc or desc order'):
    valid_fields = ['height', 'weight', 'bmi']
    valid_order = ['asc', 'desc']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,
                            detail=f'Invalid field, select from {valid_fields}')
    
    if order not in valid_order:
        raise HTTPException(status_code=400,
                            detail=f'Invalid order, select from {valid_order}')
    
    data = load_data()
    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(),
                         key=lambda x: x.get(sort_by, 0), 
                         reverse=sort_order)
    
    return sorted_data


@app.post("/create") # using post method
def create_patient(patient: Patient):
    #load existing data
    data = load_data()

    # check is the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # add new patient details to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into json file
    save_data(data)

    # returning response
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})