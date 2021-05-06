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


class FilterTestCase(unittest.TestCase):

    @staticmethod
    def filtr(e: dict) -> dict:
        return {k: v for k, v in e.items() if not k.startswith('@')}

    def test_filters(self):
        pyobj = jsonasobj.loads(test_json)
        self.assertEqual(expected, jsonasobj.as_json(pyobj, filtr=self.filtr))
        self.assertEqual(expected, pyobj._as_json_dumps(filtr=self.filtr))


if __name__ == '__main__':
    unittest.main()
