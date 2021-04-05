import os
from datetime import datetime
from flask import Flask, request, redirect, jsonify, send_file, render_template
import database
from flask_cors import CORS

app = Flask(__name__, static_folder="build")
CORS(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/home', methods=['GET'])
def home():
    response = jsonify(
        {'message': 'Welcome', "Time": datetime.now().__str__()})
    response.status_code = 200
    return response


@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    if data == None:
        email = request.form.get("email")
        password = request.form.get("password")
    else:
        try:
            email = data['email']
            password = data['password']
        except:
            response = jsonify({'message': 'input error'})
            response.status_code = 400
            return response
    if email == None or password == None:
        response = jsonify({'message': 'input error'})
        response.status_code = 400
        return response
    else:
        result = db.getUser(email, password)
        if result == {"message": "Not Exist"}:
            response = jsonify(result)
            response.status_code = 404
            return response
        else:
            del result['_id']
            del result['email']
            del result['password']
            response = jsonify(result)
            response.status_code = 200
            return response


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if data == None:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
    else:
        try:
            name = data['name']
            email = data['email']
            password = data['password']
        except:
            response = jsonify({'message': 'input error'})
            response.status_code = 400
            return response
    if email == None or password == None or name == None:
        response = jsonify({'message': 'input error'})
        response.status_code = 400
        return response
    else:
        result = db.addUser(name, email, password)
        response = jsonify(result)
        response.status_code = 201
        return response


# Check file extention if accepted
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


upload POST request
    Take  email , password and file from request body as form data
    then verify and validate file , email and password 
    then check file type if allowed
    then authenticate user and save file in ./uploads with timestamp file name
    Return uploaded file name
    Errors:
        input empty or miss or bad 400 response code
        Unauthorized user 403 response code



if __name__ == "__main__":
    app.run()
