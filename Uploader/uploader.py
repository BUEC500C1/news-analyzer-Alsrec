# upload and prosecess API(entity)



import time





# Create--> create a document
# Delete--> delete a document
# Update--> update a latest version of a document
# Read--> look the context of a document

def create(files, filename):
    if filename == None:
        print("error filename")
        return "errorfilename"
    else:
        name = filename
        createtime = time.time()
        print("create file successfully!")
        return "success"


def Delete(filename):
    if filename == NULL:
        print("error filename")
        return "errorfilename"
    else:
        return "delete file successfully!"

def Update(files, filename):
    if filename == NULL:
        print("error filename")
        return "errorfilename"
    else:
        return "update file successfully"

def read(filename):
    if filename == NULL:
        print("error filename")
        return "errorfilename"
    else:
        return "open file succseefully"
