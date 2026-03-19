from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database
from app.models import UserCreate

app = FastAPI()

# Crear tablas al iniciar la app (Desarrollo)
models.Base.metadata.create_all(bind=database.engine)

# Dependencia de DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id": user.id, "username": user.username, "email": user.email}

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Accedemos a los datos a través del objeto 'user'
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user