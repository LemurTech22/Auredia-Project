from flask import jsonify, request, Blueprint
from App.database import db, User
from App.auth import require_api_key
routes = Blueprint('routes', __name__)

#API core functionality
@routes.route('/create_user',methods =['POST'])
@require_api_key
def create_user(): 
    #Used for the Interface only
    """
    Create a new user.
    ---
    tags:
      - Users
    security:
      - ApiKeyAuth: []
    parameters:
      - in: body
        name: body
        required: true
        description: The user to create.
        schema:
          type: object
          required:
            - user_name
            - first_name
            - last_name
            - email
          properties:
            user_name:
              type: string
              description: Unique username.
            first_name:
              type: string
              description: The user's first name.
            last_name:
              type: string
              description: The user's last name.
            email:
              type: string
              description: The user's email address.
    responses:
      201:
        description: User successfully created.
        schema:
          id: User
          properties:
            id:
              type: integer
            user_name:
              type: string
            first_name:
              type: string
            last_name:
              type: string
            email:
              type: string
      400:
        description: Invalid input.
    """


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
@require_api_key
def get_user(user_id):
    
    """
   Get User information.
    ---
    tags:
      - Users
    security:
      - ApiKeyAuth: []
    parameters:
      - name: user_id
        in: path
        type: integer
        requied: True
        description: Getting the User information.
        schema:
          type: object
          required:
            - Employee ID
          properties:
            user_name:
              type: string
              description: Unique username.
            first_name:
              type: string
              description: The user's first name.
            last_name:
              type: string
              description: The user's last name.
            email:
              type: string
              description: The user's email address.
    responses:
      201:
        description: Successfully Gathered User Information.
        schema:
          id: User
          properties:
            id:
              type: integer
            user_name:
              type: string
            first_name:
              type: string
            last_name:
              type: string
            email:
              type: string
      400:
        description: User does not exist.
    """


    user = User.query.get(user_id)

    if not user:
        return jsonify({"Message": "User does not exist"}), 404
    return jsonify(user.to_dict())

@routes.route('/update_user/<int:user_id>',methods=['PUT'])
@require_api_key
def update_user(user_id):
      #Used for the Interface only

    """
   Update an existing user's information.
    ---
    tags:
      - Users
    security:
      - ApiKeyAuth: []
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: The ID of the user to update.
      - in: body
        name: body
        required: true
        description: The updated user information.
        schema:
          type: object
          properties:
            user_name:
              type: string
              description: The new username (optional).
            first_name:
              type: string
              description: The new first name (optional).
            last_name:
              type: string
              description: The new last name (optional).
            email:
              type: string
              description: The new email address (optional).
    responses:
      200:
        description: User successfully updated.
        schema:
          id: User
          properties:
            id:
              type: integer
              description: The user ID.
            user_name:
              type: string
              description: The user's username.
            first_name:
              type: string
              description: The user's first name.
            last_name:
              type: string
              description: The user's last name.
            email:
              type: string
              description: The user's email address.
      404:
        description: User not found.
    """   
    
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
    #Used for the Interface only
    """
   Deleting User Information.
    ---
    tags:
      - Users
    security:
      - ApiKeyAuth: []
    parameters:
      - name: user_id
        in: path
        type: integer
        required: True
        description: Deleting User information.
        schema:
          type: object
          required:
            - Employee ID
    responses:
      201:
        description: Successfully Deleted User Information.
        schema:
          id: User
          properties:
            id:
              type: integer
            user_name:
              type: string
            first_name:
              type: string
            last_name:
              type: string
            email:
              type: string
      400:
        description: User does not exist.
    """
    user_to_delete =  User.query.get(user_id)
    if not user_to_delete:
        return (jsonify({"Message": "User not found"}))
    db.session.delete(user_to_delete)
    db.session.commit()
    return jsonify({"Message": "User has been deleted."}), 200
