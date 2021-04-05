#app.py
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_mongoengine import MongoEngine #ModuleNotFoundError: No module named 'flask_mongoengine' = (venv) C:\flaskmyproject>pip install flask-mongoengine  
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
  
app = Flask(__name__)
app.secret_key = "jiberish"

app.config['MONGODB_SETTINGS'] = {
    'db': 'file',
    'host': 'mongodb+srv://Wodiaonima38:12345@cluster0.c0zss.mongodb.net/file?retryWrites=true&w=majority',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)    
  
UPLOAD_FOLDER = '/uplaod'
PATH = os.path.abspath('upload')
app.config['UPLOAD_FOLDER'] = PATH
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
   
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
   
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
   
class news(db.Document):
    name = db.StringField()
    email = db.StringField()
    file = db.StringField()
     
@app.route('/')
def index():
    return render_template('upload.html')
  
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    rs_username = request.form['txtusername']
    inputEmail = request.form['inputEmail']
    filename = secure_filename(file.filename)
   
    if file and allowed_file(file.filename):
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       usersave = news(name=rs_username, email=inputEmail, file =file.filename)
       usersave.save()
       flash('File successfully uploaded ' + file.filename + ' to the database!')
       return redirect('/')
    else:
       flash('Invalid Uplaod only txt, pdf, png, jpg, jpeg, gif') 
    return redirect('/')    
   
if __name__ == '__main__':
    app.run(debug=False)



