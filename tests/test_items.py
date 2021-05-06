
import unittest
import jsonasobj

test_json = """{
    "k1": 1,
    "k2": "abc",
    "k3": {
        "x1": "foo",
        "x2": 17
    }
}"""


class ItemsTestCase(unittest.TestCase):
    def test_items(self):
        py_obj = jsonasobj.loads(test_json)
        for k, v in py_obj._items():
            if k == 'k1':
                self.assertEqual(1, v)
            elif k == 'k2':
                self.assertEqual("abc", v)
            else:
                self.assertEqual(k, "k3")
                self.assertTrue(isinstance(v, jsonasobj.JsonObj))
                self.assertEqual("foo", v.x1)
                self.assertEqual(17, v.x2)

if __name__ == '__main__':
    unittest.main()
