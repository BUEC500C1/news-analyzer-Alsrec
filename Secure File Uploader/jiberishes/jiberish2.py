from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import logging
import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import os
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploaded/'

#DB cluster info
cluster = MongoClient("mongodb+srv://985552883@qq.com:qq.comcyh19980203@IP:27017/somedb?authSource=admin&readPreference=secondaryPreferred")
db = cluster["file"]
collection = db["news"]
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/uploaded', methods = ['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
        f = request.files['file']
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(filepath)
        fd = open(filepath, "rb")
        doc = PDFDocument(fd)
        version = doc.header.version
        print(doc.metadata)
        creationDate = doc.metadata.get('CreationDate')
        dataType = doc.metadata.get('Subtype')
        #data methods
        viewer = SimplePDFViewer(fd)
        textData = []
        for canvas in viewer:
            #print(canvas.strings)
            textData += canvas.strings
            tempstring = ''
            textWords = []
            for character in textData:
                if character != ' ':
                    tempstring += character
                else:
                    if tempstring:
                        textWords.append(tempstring)
                        tempstring = ''
                
        print(secure_filename(f.filename))
        print(creationDate)
        print(textWords)

        fileDocument = {
            "name" : secure_filename(f.filename),
            "creationDate" : creationDate,
            "text" : textWords
        }

        collection.insert_one(fileDocument)
        return 'file uploaded successfully'



if __name__=="__main__":
    app.run(host='0.0.0.0')
