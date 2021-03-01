
# News feed ingester API(entity)


# check_if_exist --> check if the file you want to search is exist

import flask
import json

api = Flask(__name__)

@api.route("/files/<filename>")
def check_if_exist(filename):
#    if filename does not exist, return "filename dose not exist"
#    if the status is not analysed return "file is not ready for search"
    return True

@app.route("/files/<filename>")
def search_on_web(sentiment, keywords):
    doucument = "...."
    return doucument

