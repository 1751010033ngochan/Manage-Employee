from app import db


# Create table MySQL
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __str__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


if __name__ == "__main__":
    db.create_all()