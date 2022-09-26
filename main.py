from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles

from database.db import create_table, insert_donation, get_summery
from datetime import date


total_donations = None
total_donors = None

app = FastAPI()

create_table()


class Donation(BaseModel):
    amount: float

def load_summery():
    global total_donations, total_donors
    total_donations, total_donors = get_summery()

load_summery()

@app.get("/summery")
def get_summery():
    return {"total": total_donations, "donors" : total_donors }

def validate_donation(donation : Donation):
    if (donation.amount <= 0):
        raise HTTPException(status_code=400 , detail="Donation amount should be larger than zero")


@app.post("/donations")
def add_donation(donation : Donation):
    global total_donations, total_donors

    validate_donation(donation)
    today = date.today()
    insert_donation(donation.amount, today)

    total_donations += donation.amount
    total_donors+=1

    return {}


app.mount("/", StaticFiles(directory="static", html=True), name="homepage")
