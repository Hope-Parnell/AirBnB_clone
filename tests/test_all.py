#!/usr/bin/python3
"""Test the console module"""
import unittest
import pycodestyle


class TestAll(unittest.TestCase):
    """Tests over-arching things"""
    @classmethod
    def setUpClass(cls):
        """sets up the class"""
        pass

    @classmethod
    def tearDownClass(cls):
        """cleans up the class"""
        pass

    def testPycodestyle(self):
            """Testing pycodestyle validation"""
            check = pycodestyle.StyleGuide(quiet=True)
            unittest.result = check.check_files(
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
        """tests for shebang at begining of file"""
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
                self.assertEqual(f.readline(), "#!/usr/bin/python3\n",
                    "first line is not shebang in {}".format(item))

    def testREADME(self):
        """tests for non-empty README"""
        with open("README.md") as f:
            self.assertNotEqual(len(f.read()), 0," README is empty")
        with open("tests/README.md") as f:
            self.assertNotEqual(len(f.read()), 0, "README is empty")
