#!/usr/bin/python3
""""Tests the file_storage module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel



class TestFileStorage(unittest.TestCase):
    """Class tests file_storage class"""
    def setUp(self):
        self.fs = FileStorage()

    def tearDown(self):
        with open("file.json", "w") as f:
            blankDict = {}
            f.write("{}".format(blankDict))

    def testAll(self):
        self.assertEqual(self.fs.all(), {})
        a = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263", updated_at="1020-02-13T07:10:03.134263")
        self.fs.new(a)
        self.assertEqual(self.fs.all(), {"BaseModel.69": a})

    def testNew(self):
        with self.assertRaises(TypeError): 
            self.fs.new()
    
    def testSave(self):
        #file created
        a = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263", updated_at="1020-02-13T07:10:03.134263")
        self.fs.new(a)
        self.fs.save()
        with open("file.json") as f:
            line = f.readline()
            self.assertEqual(line, '{"BaseModel.69": {"id": 69, "created_at": "1000-07-29T12:14:07.132263", "updated_at": "1020-02-13T07:10:03.134263", "__class__": "BaseModel"}}')

    def testReload(self):
        self.fs.reload()
        self.assertEqual(self.fs.all(), {})
        a = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263", updated_at="1020-02-13T07:10:03.134263")
        self.fs.new(a)
        self.fs.save()
        self.fs.reload()
        self.assertEqual(str(self.fs.all().get("BaseModel.69")), str(a))


