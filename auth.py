from flask import Blueprint, render_templete 

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "This Page will be used to sign up users"

@auth.route('/login')
def login():
    return "This Page will be used to login users"

@auth.route('/logout')
def logout():
    return "Use this to log out"
