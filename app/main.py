from fastapi import FastAPI
import markovify
import os 
import json


app = FastAPI()

def chainmake(): 
    with open('/static/corpi_json/cat_namegen.json', 'r' , encoding='utf-8' ) as file: 
        data = file.read()
    chain = json.loads(data)
    pet = markovify.Text.from_json(chain)
    return pet

@app.get("/")
def read_root():
    return {"Greeting": "welcome to pet-gen, care to create a pet?"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/pet/{length}")
async def read_pet(length: int):
    if length >= 20:
        pet = chainmake()
        response = str(pet.make_short_sentence(length, tries=100))
        if response == None:
            return{"pet_name": "no cat 4 u lol"} 
        else: 
            return{"pet_name": response} 
    else: 
        return{"message": "not long enough"}


    