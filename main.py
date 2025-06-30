# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import crud
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/recipes")
def create_recipe(recipe: dict, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe)

@app.get("/recipes")
def read_recipes(db: Session = Depends(get_db)):
    return crud.get_recipes(db)

@app.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.patch("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, updates: dict, db: Session = Depends(get_db)):
    recipe = crud.update_recipe(db, recipe_id, updates)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.delete_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Deleted successfully"}
