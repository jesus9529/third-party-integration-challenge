# 3rd API Party Integration

## Requirements
- python 3.10.*
- pip 22.*

## Instalation
### Linux users
- First, create a virtual environment using python3 venv package
```
python3 -m venv venv
```
- Activate virtual environment 
```
source venv/bin/activate
```
- Install dependencies
```
pip install -r requirements.txt
```
- Creates dotenv file
```
cp .env.sample .env
```
- Set TEST_TOKEN value with token received in email in .env file

### Windows users
- First, create a virtual environment using python3 venv package
```
python -m venv venv
```
- Activate virtual environment 
```
.\venv\Scripts\activate
```
- Install dependencies
```
pip install -r requirements.txt
```
- Creates dotenv file
```
cp .env.sample .env
```
- Set TEST_TOKEN value with token received in email in .env file

## How to run it
- Start the server with using uvicorn
```
uvicorn main:app --reload
```
- Import postman collection and environment json files in postman directory and start making request

## Endpoints
- GET /

Root endpoint to check is server is alive. Return a simple json.

- GET /members/{member_id}

Endpoint to get member data detail using a member identifier as parameter. A response example should look like:
```
{
    "api_response": {
        "dependents": [
            {
                "external_id": 89,
                "relationship": 19,
                "plancode": "11AA22BB",
                "active": true,
                "first_name": "James",
                "last_name": "McGill",
                "gender": "M",
                "street_1": "6b",
                "street_2": null,
                "city": "New york City",
                "state": "NY",
                "zipcode": "98198",
                "benefit_start": "2022-07-29",
                "dob": "2022-06-25"
            }
        ],
        "external_id": 23,
        "relationship": 18,
        "plancode": "11AA22BB",
        "active": true,
        "first_name": "John",
        "last_name": "Doe",
        "gender": "M",
        "street_1": "6b",
        "street_2": null,
        "city": "New york City",
        "state": "NY",
        "zipcode": "98198",
        "benefit_start": "2022-07-29",
        "dob": "2022-06-25"
    }
}
```
- POST /members

This endpoint allows to create a member instance

Request example
```
{
    "external_id": 23,
    "relationship": 18,
    "first_name": "John",
    "last_name": "Doe",
    "plancode": "11AA22BB",
    "dob": "2022-06-25",
    "benefit_start": "2022-07-29",
    "gender": "M",
    "street_1": "6b",
    "city": "New york City",
    "state": "NY",
    "zipcode": "98198"
}
```

Response example
```
{
    "api_response": {
        "external_id": 23,
        "relationship": 18,
        "plancode": "11AA22BB",
        "active": true,
        "first_name": "John",
        "last_name": "Doe",
        "gender": "M",
        "street_1": "6b",
        "street_2": null,
        "city": "New york City",
        "state": "NY",
        "zipcode": "98198",
        "benefit_start": "2022-07-29",
        "dob": "2022-06-25"
    }
}
```
- POST /members/{external_member_id}

This endpoint allows to create a dependant instance from an external member id

Request example
```
{
    "external_id": 89,
    "relationship": 19,
    "first_name": "James",
    "last_name": "McGill",
    "plancode": "11AA22BB",
    "dob": "2022-06-25",
    "benefit_start": "2022-07-29",
    "gender": "M",
    "street_1": "6b",
    "city": "New york City",
    "state": "NY",
    "zipcode": "98198"
}
```

Response example
```
{
    "api_response": {
        "external_id": 89,
        "relationship": 19,
        "plancode": "11AA22BB",
        "active": true,
        "first_name": "James",
        "last_name": "McGill",
        "gender": "M",
        "street_1": "6b",
        "street_2": null,
        "city": "New york City",
        "state": "NY",
        "zipcode": "98198",
        "benefit_start": "2022-07-29",
        "dob": "2022-06-25"
    }
}
```

## Extra information

To perform the request to the 3rd party api, a token is sended in headers.