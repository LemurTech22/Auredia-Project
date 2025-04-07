from flask import jsonify, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import SQLAlchemy
from App.imports import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auredia.db'


#define the database here
class User(db.Model):
    id = db.column(db.Integer,primary_key=True)
    username = db.column(db.String(100),nullable=False,unique=True)
    fname = db.column(db.String(50), nullable=False)
    Lname = db.column(db.String(50), nullable=False)
    email = db.column(db.String(100),nullable=False)
#define the route of the database
user_db = BluePrint('user',__name__)

@app.route("/")
def welcome_page():
    return render_template('index.html')
"""""
@app.route('Create User',methods =['POST'])
def create_user(): 
    global id_number
    data = request.get_json()
    user = {
        "id": id_number,
        "user_name": data.get('username'),
        'email': data.get('email')
    }

    #insert into database here
    return  jsonify(user)

@app.route('Get_User', methods=['GET'])
def get_user(user_id):
    user = 0#get database info here db.get(user_id)
    #get user where id == user_id
    if user:
        return jsonify(user)
    return jsonify({"Message": "User does not exist"}),404

@app.route('Update_User\<id>',method=['PUT'])
def update_user(user_id):
    user = 2#database call to get user by id db.get(user_id)
    if not user:
        return jsonify({"Error": "User not Found"}),404
    
    info = request.get_json()
    user['username'] = info.get("username",user['username'])
    user['email'] = info.get('email',user['email'])
    

    #update user to database by UPDATE SET WHERE id=user_ID
    return jsonify(user)

@app.route('Delete_User', methods =['DELETE'])
def delete_user(user_id):
    #get from data base the user 
    user_to_delete =  0#.pop(user_id,None)
    #run sql command to delete user by user id
    if user_to_delete:
        return (jsonify({"Message": "User Deleted"}))
    return jsonify({"error": "User not Found"}), 404
"""