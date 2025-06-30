from fastapi import FastAPI, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from database import SessionLocal
import crud

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/recipes")
def create_recipe(recipe: dict = Body(...), db: Session = Depends(get_db)):
    required = ["title", "making_time", "serves", "ingredients", "cost"]
    if not all(k in recipe for k in required):
        return {"message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost"}
    new_recipe = crud.create_recipe(db, recipe)
    return {"message": "Recipe successfully created!", "recipe": [crud.recipe_to_dict(new_recipe)]}

@app.get("/recipes")
def read_recipes(db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db)
    return {"message": "Recipe details by GET", "recipes": [crud.recipe_to_dict(r) for r in recipes]}

@app.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail={"message": "No Recipe found"})
    return {"message": "Recipe details by id", "recipe": crud.recipe_to_dict(recipe)}

@app.patch("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, updates: dict = Body(...), db: Session = Depends(get_db)):
    recipe = crud.update_recipe(db, recipe_id, updates)
    if not recipe:
        raise HTTPException(status_code=404, detail={"message": "No Recipe found"})
    return {"message": "Recipe successfully updated!", "recipe": crud.recipe_to_dict(recipe)}

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    success = crud.delete_recipe(db, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail={"message": "No Recipe found"})
    return {"message": "Recipe successfully removed!"}
