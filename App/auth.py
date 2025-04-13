from functools import wraps
from flask import request, jsonify, current_app

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        provided_key = request.headers.get('X-API-KEY')
        current_app.logger.info("Provided API Key: %s", provided_key)
        current_app.logger.info("Expected API Key: %s", current_app.config.get('API_KEY'))
        if not provided_key or provided_key != current_app.config.get('API_KEY'):
            return jsonify({'Message': "Invalid or missing API Key"}),401
        
        return f(*args,**kwargs)
    return decorated
