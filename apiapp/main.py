from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Outdoor Retailer API"}

@app.post('/predict')
def predict(make:str="Ford", model:str="F150 Pickup 4WD", year:int=2005):
    """
    Predict price based on year, manufacturer, model
    """
    manufacturer = make
    manufacturer = manufacturer.lower()
    model_lower = model.lower()

    # use fuzzy wuzzy to get the closest match
    model_fz = process.extractOne(model_lower, cl_models, scorer=fuzz.token_sort_ratio)[0]
    
    input = pd.DataFrame({
        "year": [year],
        "manufacturer": [manufacturer],
        "model": [model_fz],
        "odometer": 10000
        })
    
    pred = test_model.predict(input)

    car_price_prediction = pred[0]