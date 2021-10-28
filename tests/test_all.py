#!/usr/bin/python3
"""Test the console module"""
import unittest
import pep8


class TestAll(unittest.TestCase):
    """Tests over-arching things"""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testPep8(self):
            """Testing pep8 validation"""
            pep8style = pep8.StyleGuide(quiet=True)
            unittest.result = pep8style.check_files(
                ['models/engine/file_storage.py', 
                'models/amenity.py', 
                'models/base_model.py', 
                'models/city.py', 
                'models/place.py', 
                'models/review.py', 
                'models/state.py', 
                'models/user.py', 
                'console.py'])

            self.assertEqual(unittest.result.total_errors, 0,
                            "Found code style errors (and warnings).")
    
    def testShebang(self):
        files = ['models/engine/file_storage.py', 
                'models/amenity.py', 
                'models/base_model.py', 
                'models/city.py', 
                'models/place.py', 
                'models/review.py', 
                'models/state.py', 
                'models/user.py', 
                'console.py']
        for item in files:
            with open(item) as f:
                self.assertEqual(f.readline(), "#!/usr/bin/python3", 
                    "first line is not shebang in {}".format(item))