from fastapi import FastAPI
from petgen import classes

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Greeting": "welcome to pet-gen, care to create a pet?"}

@app.get("/cat/")
async def read_cat():
    cats = classes.CatGen() 
    return{"pet": cats.catJSON()}

@app.get("/dog/")
async def read_dog():
    dogs = classes.DogGen() 
    return{"pet": dogs.dogJSON()}