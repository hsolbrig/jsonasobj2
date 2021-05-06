
import unittest
import jsonasobj

test_json = """{
    "k1": 1,
    "k2": "abc",
    "k3": {
        "x1": "foo",
        "x2": 17
    },
    "k4": [1, "abc", {"k5": 42}]
}"""


class GetTestCase(unittest.TestCase):
    def test_get(self):
        py_obj = jsonasobj.loads(test_json)
        self.assertEqual(1, py_obj.k1)
        with self.assertRaises(AttributeError):
            py_obj.e1
        self.assertIsNone(py_obj._get('e1'))
        self.assertEqual("abc", py_obj._get('e2', 'abc'))

if __name__ == '__main__':
    unittest.main()
