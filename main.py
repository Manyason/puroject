from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Recipe
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

class RecipeCreate(BaseModel):
    title: str
    description: str

class RecipeOut(RecipeCreate):
    id: int

@app.post("/recipes", response_model=RecipeOut)
def create_recipe(recipe: RecipeCreate):
    db = SessionLocal()
    db_recipe = Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    db.close()
    return db_recipe

@app.get("/recipes", response_model=List[RecipeOut])
def get_recipes():
    db = SessionLocal()
    recipes = db.query(Recipe).all()
    db.close()
    return recipes

@app.get("/recipes/{id}", response_model=RecipeOut)
def get_recipe(id: int):
    db = SessionLocal()
    recipe = db.query(Recipe).filter(Recipe.id == id).first()
    db.close()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.patch("/recipes/{id}", response_model=RecipeOut)
def update_recipe(id: int, recipe: RecipeCreate):
    db = SessionLocal()
    db_recipe = db.query(Recipe).filter(Recipe.id == id).first()
    if db_recipe is None:
        db.close()
        raise HTTPException(status_code=404, detail="Recipe not found")
    for key, value in recipe.dict().items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    db.close()
    return db_recipe

@app.delete("/recipes/{id}")
def delete_recipe(id: int):
    db = SessionLocal()
    db_recipe = db.query(Recipe).filter(Recipe.id == id).first()
    if db_recipe is None:
        db.close()
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(db_recipe)
    db.commit()
    db.close()
    return {"detail": "Deleted"}
