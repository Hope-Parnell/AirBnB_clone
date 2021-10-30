#!/usr/bin/python3
"""Test the console module"""
import unittest
import pycodestyle
import os


class TestAll(unittest.TestCase):
    """Tests over-arching things"""
    def setUp(self):
        """sets up the class"""
        self.files = ['models/engine/file_storage.py',
                      'models/amenity.py',
                      'models/base_model.py',
                      'models/city.py',
                      'models/place.py',
                      'models/review.py',
                      'models/state.py',
                      'models/user.py',
                      'console.py']
        pass

    def tearDown(self):
        """cleans up the class"""
        pass

    def testPycodestyle(self):
        """Testing pycodestyle validation"""
        check = pycodestyle.StyleGuide(quiet=True)
        unittest.result = check.check_files(self.files)

        self.assertEqual(unittest.result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testShebang(self):
        """tests for shebang at begining of file"""
        for item in self.files:
            with open(item) as f:
                self.assertEqual(f.readline(), "#!/usr/bin/python3\n",
                                 "first line needs shebang in {}".format(item))

    def testExecutable(self):
        for item in self.files:
            self.assertTrue(os.access(item, os.X_OK),
                            "File {} is not executable".format(item))
