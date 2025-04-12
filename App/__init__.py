from flask import Flask
from App.config import app as configured_app
from App.database import db
from App.routes import routes


def create_app():
    app = configured_app
    db.init_app(app)
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()
    return app