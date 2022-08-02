from datetime import date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Member(BaseModel):
    external_id: int = Field(gt=0)
    relationship: int = Field(gt=17, lt=19)
    first_name: str
    last_name: str
    gender: str
    plancode: str
    street_1: str
    street_2: Optional[str]
    city: str
    state: str
    zipcode: str
    dob: date
    benefit_start: date

class Dependant(Member):
    relationship: int = Field(gt=18, lt=20)
