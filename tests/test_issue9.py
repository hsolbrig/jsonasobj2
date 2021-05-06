import unittest
from copy import deepcopy
from dataclasses import dataclass

from jsonasobj import JsonObj


class YAMLRoot(JsonObj):
    pass


@dataclass
class Test(YAMLRoot):
    v: int


class MissingConstructorTestCase(unittest.TestCase):
    def test_missing_constructor(self):
        """ Test for reasonable behavior when the constructor wasn't invoked """
        z = Test(1)
        deepcopy(z)     # Invokes test for local __deepcopy__ in z


if __name__ == '__main__':
    unittest.main()
