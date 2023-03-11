import unittest
from getMALtoken import getMALtoken

class TestgetMALtoken(unittest.TestCase):
    def test_get_new_code_verifier(self):
        self.assertIsNotNone(getMALtoken.get_new_code_verifier)
        
    def test_print_new_authorisation_url(self):
        code = getMALtoken.get_new_code_verifier
        self.assertIsNotNone(getMALtoken.print_new_authorisation_url(self, code_challenge=code))