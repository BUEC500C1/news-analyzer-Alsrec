import os
from datetime import datetime
from flask import Flask, request, redirect, jsonify, send_file, render_template
import database
from flask_cors import CORS

app = Flask(__name__, static_folder="build")
CORS(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

"""Test connection GET request
   Return json message for connection test
"""
@app.route('/home', methods=['GET'])
def home():
    response = jsonify(
        {'message': 'Welcome', "Time": datetime.now().__str__()})
    response.status_code = 200
    return response

# Authintecation


"""Sing in POST request
    Take email and password from request body as form data or json
    then verify and validate email and password
    Return user data with 200 OK response code
    Errors:
        User not found 404 response code
        input empty or miss 400 response code
"""
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


"""Sing up POST request
    Take name , email and password from request body as form data or json
    then verify and validate name , email and password then add user to database
    Return json message with 201 OK response code
    Errors:
        input empty or miss 400 response code
"""
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


""" File GET request
    Take Uploaded Filename as request parameter
    Return file if exist 200 code response
"""
@app.route('/files/<filename>', methods=['GET'])
def files(filename):
    response = send_file(os.path.join(
        "./uploads", filename), as_attachment=True)
    response.status_code = 200
    return response


"""upload POST request
    Take  email , password and file from request body as form data
    then verify and validate file , email and password 
    then check file type if allowed
    then authenticate user and save file in ./uploads with timestamp file name
    Return uploaded file name
    Errors:
        input empty or miss or bad 400 response code
        Unauthorized user 403 response code
"""
@app.route('/upload', methods=['POST'])
def upload_file():
    email = request.form.get("email")
    password = request.form.get("password")
    method = request.form.get("method")
    print(method)
    if email == None or password == None:
        response = jsonify({'message': 'Unauthorized'})
        response.status_code = 403
        return response
    else:
        result = db.getUser(email, password)
        if result == {"message": "Not Exist"}:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = 403
            return response
        else:
            if 'file' not in request.files:
                response = jsonify({'message': 'No file part in the request'})
                response.status_code = 400
                return response
            file = request.files['file']
            if file.filename == '':
                response = jsonify(
                    {'message': 'No file selected for uploading'})
                response.status_code = 400
                return response
            if file and allowed_file(file.filename):
                filename = datetime.now().timestamp().__int__().__str__()
                filename = filename + "."
                file.filename.split('.', 1)[1].lower()
                file.save(os.path.join("./uploads", filename))
                db.addphoto(email=email, password=password,
                            photoName=filename)
                response = filename
                return response
            else:
                response = jsonify(
                    {'message': 'Allowed file types are png, jpg, jpeg'})
                response.status_code = 400
                return response


if __name__ == "__main__":
    app.run()
