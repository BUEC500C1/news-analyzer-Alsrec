from uploader import *

def test_create():
  assert create(1, None) == "errorfilename"
  assert create(1, "hellow") == "success"
  
def test_Delete():
  assert Delete(None) == "errorfilename"
  assert Delete({hellow") == "delete file successfully!"
  
def test_Update():
  assert Update(None) == "errorfilename"
  assert Update("hellow") == "update file successfully"

def test_read():
  assert read(None) == "errorfilename"
  assert read("hellow") == "open file succseefully"
  


