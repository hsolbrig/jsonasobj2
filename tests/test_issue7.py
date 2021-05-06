import json
import unittest

from jsonasobj import JsonObj, loads, as_json, as_json_obj, as_dict

s_list = '''[
   {
      "a": 17,
      "b": "sell",
      "c": [
         1,
         2,
         3
      ],
      "d": null,
      "e": {},
      "f": {
         "g": -12.56
      }
   },
   143
]'''

p_list = [{'a': 17, 'b': 'sell', 'c': [1, 2, 3], 'd': None, 'e': {}, 'f': {'g': -12.56}}, 143]


class OuterListTestCase(unittest.TestCase):
    """ Test various forms of outermost lists """
    def test_loads_list(self):
        t1 = loads(s_list)
        self.assertEqual(p_list, as_json_obj(t1))
        self.assertEqual(s_list, as_json(t1))

    def test_list_constructor(self):
        t1 = loads(s_list)
        t1_dict = as_json_obj(t1)
        self.assertEqual(p_list, t1_dict)
        t2 = JsonObj(t1_dict)
        self.assertEqual(s_list, as_json(t2))

    def test_list_subscripts(self):
        t1 = loads(s_list)
        self.assertEqual(3, t1[0].c[2])
        self.assertEqual(-12.56, t1[0].f.g)

    @unittest.skip("Setters have yet to be implemented")
    def test_list_setters(self):
        t1 = JsonObj([])
        print(t1)
        t1.append('14')
        print(as_json(t1))


if __name__ == '__main__':
    unittest.main()
