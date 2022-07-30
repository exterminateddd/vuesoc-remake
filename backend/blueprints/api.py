from flask import Blueprint, jsonify, request
from database.models import db, User, Post
from utils import hash_password as hashpw

api = Blueprint("api", "api")


@api.route("/ping", methods=["GET"])
def ping_route():
    return jsonify("Pong!"), 200


@api.route("/users", methods=["GET"])
def get_users_route():
    users = db.session.query(User).all()

    return jsonify([u.to_dict() for u in users]), 200


@api.route("/posts", methods=["GET"])
def get_posts_route():
    posts = db.session.query(Post).all()

    return jsonify([u.to_dict() for u in posts]), 200
