from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100),nullable=False)

    def to_dict(self):
        return {"id": self.id, 
                "username": self.username,
                "fname": self.fname,
                "lname": self.lname,
                "email": self.email}