from routes import routes
from config import app
from database import db
#def main():
    
db.init_app(app)

app.register_blueprint(routes)

def create_tables():
    db.create_all()

if __name__ == '__main__':
    #main()
    app.run(debug=True)