from petgen import classes  
from database import auth, models

cats = classes.CatGen() 

print(cats.catJSON())

models.createdb() 
