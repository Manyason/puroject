from models import Recipe
from sqlalchemy.orm import Session

def recipe_to_dict(r):
    return {
        "id": r.id,
        "title": r.title,
        "making_time": r.making_time,
        "serves": r.serves,
        "ingredients": r.ingredients,
        "cost": str(r.cost),
        "created_at": str(r.created_at),
        "updated_at": str(r.updated_at)
    }

def create_recipe(db: Session, data: dict):
    recipe = Recipe(
        title=data["title"],
        making_time=data["making_time"],
        serves=data["serves"],
        ingredients=data["ingredients"],
        cost=data["cost"]
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def get_recipes(db: Session):
    return db.query(Recipe).all()

def get_recipe(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def update_recipe(db: Session, recipe_id: int, updates: dict):
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        return None
    for k, v in updates.items():
        setattr(recipe, k, v)
    db.commit()
    db.refresh(recipe)
    return recipe

def delete_recipe(db: Session, recipe_id: int):
    recipe = get_recipe(db, recipe_id)
    if not recipe:
        return False
    db.delete(recipe)
    db.commit()
    return True
