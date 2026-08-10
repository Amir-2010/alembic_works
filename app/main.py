
from fastapi import FastAPI,Depends
from database import Base,engine,person,get_data
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
@app.get("/")
def show_data(user_name:str|None=None,db:Session=Depends(get_data)):
    query = db.query(person)
    if user_name is None:
        return query.all()

    user_data = query.filter(person.name == user_name).one_or_none()
    if user_data is not None:
        return user_data
    else:
        return {"detail": "user not found"}

@app.post("/")
def add_user(user_name:str|None=None,db:Session=Depends(get_data)):
    query = db.query(person)
    check_duplicate = query.where(person.name==user_name).one_or_none()
    if check_duplicate == None:
        user = person(name=user_name)
        db.add(user)
        db.commit()
        user_data = query.where(person.name==user_name).one_or_none()
        return user_data
    else:
        return {"detail":"duplicate name"}