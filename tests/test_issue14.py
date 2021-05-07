import unittest

from jsonasobj2 import JsonObj, as_dict, as_json, is_dict, is_list


class ListTestCase(unittest.TestCase):
    def test_list(self):
        # Lists exhibit much the same behavior
        sample2 = JsonObj([dict(name="John", age=12), "pint of milk"])
        self.assertFalse(isinstance(sample2, list))
        self.assertTrue(isinstance(sample2, (list, JsonObj)))
        self.assertFalse(is_dict(sample2))
        self.assertTrue(is_list(sample2))
        self.assertEqual([{'name': 'John', 'age': 12}, 'pint of milk'], as_dict(sample2))
        self.assertEqual("""[
   {
      "name": "John",
      "age": 12
   },
   "pint of milk"
]""", as_json(sample2))


if __name__ == '__main__':
    unittest.main()
