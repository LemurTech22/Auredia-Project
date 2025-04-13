from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    employee_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(100),nullable=False,unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100),nullable=False)

    def to_dict(self):
        return {"id": self.employee_id, 
                "user_name": self.user_name,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email}