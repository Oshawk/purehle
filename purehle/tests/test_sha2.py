from purehash import sha256, sha512

from purehle._util import random_tests
from purehle.algorithms._sha2 import SHA256, SHA512


def test_sha256():
    random_tests(sha256, SHA256, (55, 56, 57, 63, 64, 65))


def test_sha512():
    random_tests(sha512, SHA512, (111, 112, 113, 127, 128, 129))
