# upload and prosecess API(entity)



import flask
import json
import time
import os

UPLOAD_DIRECTORY = "/document"
api = Flask(__name__)


# Create--> create a document
# Delete--> delete a document
# Update--> update a latest version of a document
# Read--> look the context of a document
@api.route("/files/<filename>", methods=["POST"])
def create(filename):
    """creat and upload a file"""
    if filename == None:
        print("error filename")
        return "errorfilename"
    
    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    name = filename
    createtime = time.time()
    print("create file successfully!")
    return "success"

@api.route("/files/<filename>", methods=["DELETE"])
def delete(filename):
    if filename == None:
        print("error filename")
        return "errorfilename"
    else:
        return "delete file successfully!"

@api.route('/update')
def update(files, filename):
    if filename == None:
        print("error filename")
        return "errorfilename"
    else:
        return "update file successfully"

@api.route('/read')
def read(filename):
    if filename == None:
        print("error filename")
        return "errorfilename"
    else:
        return "open file succseefully"


