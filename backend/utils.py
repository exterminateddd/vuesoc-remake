from hashlib import sha224
from json import load
from cerberus import Validator
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity


def get_jwt_identity_if_logged_in():
    try:
        verify_jwt_in_request()
        return get_jwt_identity()
    except Exception:
        return None


def hash_password(s: str):
    hashed = sha224(bytes(s.encode('utf-8'))).hexdigest()
    return hashed


def get_schemas():
    return load(open('./validation_schemas.json'))


def validate(form: str, data: dict):
    v = Validator(get_schemas()[form])
    result = v.validate(data)
    return {
        "valid": result,
        "errors": v.errors
    }
