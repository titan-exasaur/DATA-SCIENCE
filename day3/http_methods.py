import json
from fastapi import FastAPI, Path, Query, HTTPException
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Patient Management Systems API"}

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