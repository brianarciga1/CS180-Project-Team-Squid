import unittest
from getMALtoken import getMALtoken

# The main goal of this test is to testing if we can get the code verifier and auth_url before user's permission
class TestgetMALtoken(unittest.TestCase):
    # make sure get the new code veridier
    def test_get_new_code_verifier(self):
        self.assertIsNotNone(getMALtoken.get_new_code_verifier)
        
    # make sure print out the url
    def test_print_new_authorisation_url(self):
        code = getMALtoken.get_new_code_verifier
        self.assertIsNotNone(getMALtoken.print_new_authorisation_url(self, code_challenge=code))