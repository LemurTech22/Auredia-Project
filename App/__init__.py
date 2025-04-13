from flask import Flask
from App.config import app as configured_app
from App.database import db
from App.routes import routes
from flasgger import Swagger


def create_app():
    app = configured_app
    db.init_app(app)
    app.register_blueprint(routes)
    template = {
        "swagger": "2.0",
        "info": {
            "title": "User Management API",
            "description": "API for managing users with API key authentication",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "X-API-KEY"
            }
        },
        "security": [
            {"ApiKeyAuth": []}
        ]
    }
    Swagger(app,template = template)
    with app.app_context():
        db.create_all()
    return app