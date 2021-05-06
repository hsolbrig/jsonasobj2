import unittest

from jsonasobj import JsonObj, as_json, as_dict

indict = {
    "a": "a",
    "b": {
        "c": "x",
        "d": 1
    }
}

class NestedDictTestCase(unittest.TestCase):

    def test_issue_8(self):
        """ Inner elements aren't loaded as JSON objects """
        injson = JsonObj(indict)
        self.assertTrue(isinstance(injson.b, JsonObj))
        self.assertEqual(indict, as_dict(injson))


if __name__ == '__main__':
    unittest.main()
