# crud.py
from sqlalchemy.orm import Session
from models import Recipe

def get_recipes(db: Session):
    return db.query(Recipe).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def create_recipe(db: Session, recipe: dict):
    db_recipe = Recipe(**recipe)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def update_recipe(db: Session, recipe_id: int, updates: dict):
    db_recipe = get_recipe(db, recipe_id)
    if db_recipe:
        for key, value in updates.items():
            setattr(db_recipe, key, value)
        db.commit()
        db.refresh(db_recipe)
    return db_recipe

def delete_recipe(db: Session, recipe_id: int):
    db_recipe = get_recipe(db, recipe_id)
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe
