from app.models import *


def create(name, email, phone):
    employee = Data(name=name, email=email, phone=phone)

    db.session.add(employee)
    db.session.commit()


def delete_by_id(id):
    emp = Data.query.get(id)

    db.session.delete(emp)
    db.session.commit()





