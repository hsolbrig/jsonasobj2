import unittest

import jsonasobj

test_data = {
    "@context": {
        "name": "http://xmlns.com/foaf/0.1/name",
        "knows": "http://xmlns.com/foaf/0.1/knows",
        "menu": {
            "@id": "name:foo",
            "@type": "@id"
        }
    },
    "@id": "http://me.markus-lanthaler.com/",
    "name": "Markus Lanthaler",
    "knows": [
        {
            "name": "Dave Longley",
            "menu": "something",
            "modelDate" : "01/01/2015"
        }
    ]
}
test_json = str(test_data).replace("'", '"')

expected='''{
   "name": "Markus Lanthaler",
   "knows": [
      {
         "name": "Dave Longley",
         "menu": "something",
         "modelDate": "01/01/2015"
      }
   ]
}'''


class MissingObjectTestCase(unittest.TestCase):
    def test_missing(self):
        pyobj = jsonasobj.loads(test_json)
        self.assertEqual('Markus Lanthaler', pyobj.name)
        self.assertEqual(pyobj.name, pyobj['name'])
        with self.assertRaises(AttributeError) as e:
            self.assertEqual('Markus Lanthaler', pyobj.missing_item1)
        self.assertIn("object has no attribute 'missing_item1'", str(e.exception))
        with self.assertRaises(KeyError) as e:
            pyobj['12345']
        self.assertIn("'12345'", str(e.exception))
        pyobj._if_missing = lambda obj, item: (True, f"Missing: {item}")
        self.assertEqual("Missing: missing_item1", pyobj.missing_item1)
        self.assertEqual("Missing: 12345", pyobj['12345'])


if __name__ == '__main__':
    unittest.main()
