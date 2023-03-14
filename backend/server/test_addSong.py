import unittest
from addSong import addSong
from flask import session

class TestgetMALtoken(unittest.TestCase):
    def test_test(self):
        print(session['token_info'])