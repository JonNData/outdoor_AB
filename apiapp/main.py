from fastapi import FastAPI
from joblib import load

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Outdoor Retailer API"}

@app.post('/predict')
def predict(
    day_of_week:int=1, hour:int=10, visit_day:int=29, visit_num:int=1,
    First_Visit:int=1, IPD:int=0, operating_system_family:str='Windows 7',
    browser_family:str='Chrome', user_State:str='KS', 
    pageviews_before_popup:int=6, time_before_popup:float=0.0041,
    hits_before_popup:int=13, loyalty_user:bool=False
):
    """
    Predict price based on year, manufacturer, model
    """
    
    
    input = pd.DataFrame({
        "year": [year],
        "manufacturer": [manufacturer],
        "model": [model_fz],
        "odometer": 10000
        })
    
    pred = test_model.predict(input)

    car_price_prediction = pred[0]