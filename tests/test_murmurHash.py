from unittest import TestCase
from streamlib.hashes import MurmurHash


class TestMurmurHash(TestCase):
    def test_hash(self):
        mmh = MurmurHash()
        self.assertEqual(mmh.hash(10), mmh.hash(10))
