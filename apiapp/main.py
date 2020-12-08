from fastapi import FastAPI
from joblib import load
import pandas as pd

app = FastAPI()
lr_model = load("lr_classifier.joblib")

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
    Predict probability of upsell based on many factors
    """

    
    df = pd.DataFrame({
        'day_of_week': [day_of_week],
        'hour': [hour],
        'visit_day': [visit_day],
        'visit_num': [visit_num],
        'First_Visit': [First_Visit],
        'IPD': [IPD],
        'operating_system_family': [operating_system_family],
        'browser_family': [browser_family],
        'user_State': [user_State],
        'pageviews_before_popup': [pageviews_before_popup],
        'time_before_popup': [time_before_popup],
        'hits_before_popup': [hits_before_popup],
        'loyalty_user': [loyalty_user]
        })
    
    pred = lr_model.predict_proba(df)
    probability = pred[0][1]

    return {'Percent chance of upsell': round(probability*100, 2)}