from uploader import *

def test_create():
  assert create(1, NULL) == "errorfilename"
  assert create(1, "hellow") == "success"
  
def test_Delete():
  assert Delete(NULL) == "errorfilename"
  assert Delete({hellow") == "delete file successfully!"
  
def test_Update():
  assert Update(NULL) == "errorfilename"
  assert Update("hellow") == "update file successfully"

def test_read():
  assert read(NULL) == "errorfilename"
  assert read("hellow") == "open file succseefully"
  


