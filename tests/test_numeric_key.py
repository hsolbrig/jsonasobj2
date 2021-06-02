import unittest

from jsonasobj2 import JsonObj, as_json


class KeyParseTestCase(unittest.TestCase):
    def test_init_as_dict(self):
        x = JsonObj({0: "test"})
        self.assertEqual('{"0": "test"}', as_json(x, indent=None))


if __name__ == '__main__':
    unittest.main()
