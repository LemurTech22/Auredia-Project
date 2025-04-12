from flask import jsonify, request, Blueprint
from App.database import db, User

routes = Blueprint('routes', __name__)

#define the database here

#creates a user and inserts into database
@routes.route('/create_user',methods =['POST'])
def create_user(): 
    data = request.get_json()
    user = User(
        username=data['username'],
        fname=data['fname'],
        lname=data['lname'],
        email=data['email']
        )

    #insert into database changes here
    db.session.add(user)
    db.session.commit()
    #return a new user in a json with a status of creating a new user.
    return  jsonify(user.to_dict()), 201
    
#get a user information
@routes.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)#get database info here db.get(user_id)

    if not user:
        return jsonify({"Message": "User does not exist"}), 404
    return jsonify(user.to_dict())

#update the user information
@routes.route('/update_user/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)#database call to get user by id db.get(user_id)
    if not user:
        return jsonify({"Error": "User not Found"}),404
    
    info = request.get_json()
    user.username = info.get("username",user.username)
    user.email = info.get('email',user.email)

    db.session.commit()
    return jsonify(user.to_dict())
#delete user 
@routes.route('/delete_user/<int:user_id>', methods =['DELETE'])
def delete_user(user_id):
    #get from data base the user 
    user_to_delete =  User.query.get(user_id)
    #run sql command to delete user by user id
    if not user_to_delete:
        return (jsonify({"Message": "User not found"}))
    db.session.delete(user_to_delete)
    db.session.commit()
    return jsonify({"Message": "User has been deleted."}), 404