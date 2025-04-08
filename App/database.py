from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.column(db.Integer,primary_key=True)
    username = db.column(db.String(100),nullable=False,unique=True)
    fname = db.column(db.String(50), nullable=False)
    lname = db.column(db.String(50), nullable=False)
    email = db.column(db.String(100),nullable=False)

    def to_dict(self):
        return {"id": self.id, 
                "username": self.username,
                "fname": self.fname,
                "lname": self.lname,
                "email": self.email}