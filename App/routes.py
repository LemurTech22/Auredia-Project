from flask import jsonify, request, Blueprint
from App.database import db, User

routes = Blueprint('routes', __name__)

#API core functionality
@routes.route('/create_user',methods =['POST'])
def create_user(): 
    data = request.get_json()
    user = User(
        user_name=data['user_name'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email']
        )
    db.session.add(user)
    db.session.commit()
    return  jsonify(user.to_dict()), 201
    
@routes.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"Message": "User does not exist"}), 404
    return jsonify(user.to_dict())

@routes.route('/update_user/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"Error": "User not Found"}),404
    
    info = request.get_json()
    user.user_name = info.get("user_name",user.user_name)
    user.first_name = info.get("first_name", user.first_name)
    user.last_name = info.get("last_name", user.last_name)
    user.email = info.get('email',user.email)

    db.session.commit()
    return jsonify(user.to_dict())

@routes.route('/delete_user/<int:user_id>', methods =['DELETE'])
def delete_user(user_id):
    user_to_delete =  User.query.get(user_id)
    if not user_to_delete:
        return (jsonify({"Message": "User not found"}))
    db.session.delete(user_to_delete)
    db.session.commit()
    return jsonify({"Message": "User has been deleted."}), 200
