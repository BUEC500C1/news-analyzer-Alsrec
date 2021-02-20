from uploader import *

def test_create():
  assert create(1, None) == "errorfilename"
  assert create(1, "hellow") == "success"
  
def test_delete():
  assert delete(None) == "errorfilename"
  assert delete("hellow") == "delete file successfully!"
  
def test_update():
  assert update(None) == "errorfilename"
  assert update("hellow") == "update file successfully"

def test_read():
  assert read(None) == "errorfilename"
  assert read("hellow") == "open file succseefully"
  


