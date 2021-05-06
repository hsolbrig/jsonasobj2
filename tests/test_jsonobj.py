import unittest
import json
from dict_compare import compare_dicts

import jsonasobj
from jsonasobj._jsonobj import as_json, as_dict

test_json = """{
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
}"""


class BasicFunctionsTestCase(unittest.TestCase):
    """ Test the basic JSON access for the JSON-LD source
    """
    def test_basic_json_read(self) -> None:
        """ Test the basic JSON level read
        """
        py_obj = jsonasobj.loads(test_json)
        self.assertEqual("Markus Lanthaler", py_obj.name)
        self.assertEqual("Dave Longley", py_obj.knows[0].name)
        self.assertEqual("http://xmlns.com/foaf/0.1/name", py_obj["@context"].name)
        self.assertEqual("http://me.markus-lanthaler.com/", py_obj["@id"])

    def test_as_json(self):
        """ Test the JSON serialization
        """
        py_obj = jsonasobj.loads(test_json)
        self.assertEqual(json.loads(test_json), json.loads(py_obj._as_json))
        self.assertEqual(json.loads(test_json), json.loads(as_json(py_obj)))

    def test_setdefault(self):
        py_obj = jsonasobj.JsonObj()
        py_obj._setdefault('test', dict(foo=17))
        py_obj._setdefault('test', 'nada')
        py_obj._setdefault('test2', 'sama')
        self.assertTrue(compare_dicts(dict(test=dict(foo=17), test2="sama"), py_obj._as_dict))
        self.assertTrue(compare_dicts(dict(test=dict(foo=17), test2="sama"), as_dict(py_obj)))
