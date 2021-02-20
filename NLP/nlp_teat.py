from npl import *

def getsentiment_test():
  assert getsentiment("hellow") == "postive"
 
def getkeywords_test():
  assert getkeywords("hellow") == "US"
