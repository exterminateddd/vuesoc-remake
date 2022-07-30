from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, unset_jwt_cookies

from datetime import timedelta

from utils import validate, get_jwt_identity_if_logged_in, hash_password as hashpw
from database import db, User
from APIResponse import APIResponse
from UserLoginData import UserLoginData

auth = Blueprint("auth", "auth")


@auth.route("/login", methods=["POST"])
def login_route():
    resp = APIResponse()
    json = request.get_json(force=True)
    print(json, 'requested')
    json = UserLoginData(json)

    try:
        user_data = json.get("user_data", None)
        if user_data is None:
            raise Exception("no_data")
        if get_jwt_identity_if_logged_in():
            raise Exception("in_already")
        
        login_mode = json.get('mode')
        if login_mode not in ['email', 'username']:
            raise Exception('data_invalid')
    
        validation_result = validate(f"login_by_{login_mode}", user_data)
        if validation_result == False:
            raise Exception('data_invalid')
        user = User.query.filter_by(**{login_mode: user_data.get(login_mode)}).first()
        
        if not user.authenticate(user_data.get('password')):
            raise Exception('password_wrong')
        
        access_token = create_access_token(identity=user.username)
        resp.data['access_token'] = access_token

        print('user logged in', user)

        resp.success = True
    except Exception as e:
        resp.add_error(e.args[0])

    return jsonify(resp.to_dict())


@auth.route("/register", methods=["POST"])
def register_route():
    resp = APIResponse()
    json = request.get_json(force=True)
    try:
        user_data = json.get("user_data", None)
        if user_data is None:
            raise Exception("no_data")
        if get_jwt_identity_if_logged_in():
            raise Exception("in_already")
        
        validation_result = validate("register", user_data)
        if validation_result == False:
            raise Exception('data_invalid')
        user = User(username=user_data.get('username'), password=hashpw(user_data.get('password')))
        db.session.add(user)
        db.session.commit()

        # login user TODO
        resp.success = True
        
    except Exception as e:
        resp.add_error(e.args[0])
    
    return jsonify(resp.to_dict())


@auth.route('/logout', methods=["POST"])
def logout_route():
    resp = APIResponse()
    resp.data = {}
    print(resp.to_dict(), "dasdasdas")
    proccessed_response = jsonify(resp.to_dict())
    print(proccessed_response.data)
    try:
        if not get_jwt_identity_if_logged_in():
            raise Exception("out_already")
        
        unset_jwt_cookies(response=proccessed_response)

        resp.success = True
    except Exception as e:
        resp.add_error(e.args[0])
    
    print(proccessed_response.data)
    return proccessed_response


@auth.route('/current_user', methods=["GET"])
@jwt_required(optional=True)
def current_user_route():
    resp = APIResponse()
    try:
        identity = get_jwt_identity()
        user = User.query.filter_by(username=identity).first()

        resp.data = user.to_dict()
        resp.success = True
    except Exception as e:
        resp.add_error(e.args[0])
    
    return jsonify(resp.to_dict())
