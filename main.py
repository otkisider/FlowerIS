import os
from models.Client import Client
from models.database import DATABASE_NAME, Session
import create_database as db_creator
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse

# def load_data(db: Session):
#     oleg = Client(first_name="Oleg", last_name="Oleg", email="Oleg@gmail.com", address="Olegovsk d.15", discount=5)
#     db.add(oleg)
#     db.commit()
#     print(oleg.id)


# def query_data(db: Session):
#     clients = db.query(Client).all()
#     for c in clients:
#         print(f"{c.id}.{c.first_name} ({c.last_name}), ({c.email}), ({c.address}), ({c.discount})")
#

# def get_data(db: Session):
#     first_client = db.get(Client, 1)
#     print(f"{first_client.id}.{first_client.first_name} ({first_client.last_name}), ({first_client.email}),"
#           f" ({first_client.address}), ({first_client.discount})")
#     print(first_client)

#
# def delete_data(db: Session):
#     del_client = db.query(Client).filter(Client.id == 2).first()
#     db.delete(del_client)
#     db.commit()
#     print(del_client.id)


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    # get_data(Session())
    if not db_is_created:
        db_creator.create_database()
        # load_data(Session())
        # query_data(Session())
        # get_data(Session())

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("public/index.html")


@app.get("/api/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()


@app.get("/api/clients/{id}")
def get_client(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    client = db.query(Client).filter(Client.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if client == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, отправляем его
    return client


@app.post("/api/clients")
def create_client(data=Body(), db: Session = Depends(get_db)):
    client = Client(first_name=data["first_name"], last_name=data["last_name"], email=data["email"],
                    address=data["address"], discount=data["discount"])
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


@app.put("/api/clients")
def edit_client(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    client = db.query(Client).filter(Client.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if client == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    client.first_name = data["first_name"]
    client.last_name = data["last_name"]
    client.email = data["email"]
    client.address = data["address"]
    client.discount = data["discount"]
    db.commit()  # сохраняем изменения
    db.refresh(client)
    return client


@app.delete("/api/clients/{id}")
def delete_client(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    client = db.query(Client).filter(Client.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if client == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    # если пользователь найден, удаляем его
    db.delete(client)  # удаляем объект
    db.commit()  # сохраняем изменения
    return client
