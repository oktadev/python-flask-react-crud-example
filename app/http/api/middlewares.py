from functools import wraps
from flask import request, g, abort
from jwt import decode, exceptions
import json

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        authorization = request.headers.get("authorization", None)
        if not authorization:
            return json.dumps({'error': 'no authorization token provied'}), 401, {'Content-type': 'application/json'}
        
        try:
            token = authorization.split(' ')[1]
            resp = decode(token, None, verify=False, algorithms=['HS256'])
            g.user = resp['sub']
        except exceptions.DecodeError as identifier:
            return json.dumps({'error': 'invalid authorization token'}), 401, {'Content-type': 'application/json'}
        
        return f(*args, **kwargs)
   
    return wrap