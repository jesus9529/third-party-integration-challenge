import json
import os
import requests
from dotenv import load_dotenv
from fastapi import Body, FastAPI
from fastapi.encoders import jsonable_encoder
from models.models import Member, Dependant


load_dotenv()


app = FastAPI()


BASE_URL = os.environ.get("BASE_URL")
TEST_TOKEN = os.environ.get("TEST_TOKEN")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/members/{member_id}")
async def get_member_by_id(member_id: int):
    get_member_url = f"{BASE_URL}members/{str(member_id)}"
    response = requests.get(get_member_url, headers=get_headers())
    return build_response(response)


@app.post("/members")
async def create_member(data: Member):
    print(data)
    create_member_url = f"{BASE_URL}members"
    dict_data = jsonable_encoder(data)
    response = requests.post(
        create_member_url,
        data=json.dumps(dict_data),
        headers=get_headers()
    )
    return build_response(response)


@app.post("/members/{external_member_id}")
async def create_member(data: Dependant, external_member_id: int):
    print(data)
    create_member_url = f"{BASE_URL}members/{str(external_member_id)}"
    dict_data = jsonable_encoder(data)
    response = requests.post(
        create_member_url,
        data=json.dumps(dict_data),
        headers=get_headers()
    )
    return build_response(response)


###################
## Utils methods ##
###################


def get_headers():
    return {
        "Authorization": TEST_TOKEN,
        "content-type": "application/json",
    }


def build_response(response):
    return {
        "api_response": response.json()
    }
