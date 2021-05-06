import json
import os
import unittest
from typing import Callable

from dict_compare import dict_compare

from jsonasobj import as_json_obj, as_dict, as_json, get, setdefault, JsonObj, keys, items, values
from jsonasobj import loads as jso_loads, load as jso_load


CWD = os.path.dirname(__file__)
INPUT_DIR = os.path.join(CWD, 'input')


class NonJSONObjTestCase(unittest.TestCase):

    def _check_results(self, xjo: JsonObj, f: Callable[[JsonObj], dict]) -> None:
        self.assertTrue(isinstance(xjo, JsonObj))
        self.assertTrue(isinstance(xjo.a, JsonObj))
        self.assertTrue(isinstance(xjo['a'], JsonObj))
        self.assertTrue(isinstance(xjo.a.b, JsonObj))
        self.assertTrue(isinstance(xjo['a']['b'], JsonObj))
        self.assertEqual(17, xjo.a.b.c)
        self.assertEqual(17, xjo['a'].b['c'])

        xd = f(xjo)
        self.assertTrue(isinstance(xd, dict))
        self.assertTrue(isinstance(xd['a'], dict))
        self.assertTrue(isinstance(xd['a']['b'], dict))
        self.assertEqual(17, xd['a']['b']['c'])

    def test_deep_nesting(self):
        """ Make sure that the constructor does JsonObjs all the way down """
        self._check_results(JsonObj({"a": {"b": {"c": 17}}}), as_dict)

    def test_deep_nesting_loads(self):
        """ Make sure that the loads constructor does JsonObjs all the way down """
        self._check_results(jso_loads('{"a": {"b": {"c": 17}}}'), as_dict)

    def test_as_json_obj(self):
        """ Make sure the as_json_obj produces a pure dictionary """
        self._check_results(jso_loads('{"a": {"b": {"c": 17}}}'), as_json_obj)

    def test_non_jsonasobj_idioms(self):
        """ Make sure that the helper functions work with both JSONObjs and plain old JSON dicts """
        for fname in os.listdir(INPUT_DIR):
            if fname.endswith('.json'):
                fpath = os.path.join(INPUT_DIR, fname)
                with open(fpath) as f:
                    json_repr = json.load(f)
                jsonasobj_repr = jso_load(fpath)
                self.assertTrue(dict_compare(json_repr, as_json_obj(jsonasobj_repr)))
                self.assertTrue(dict_compare(json_repr, as_json_obj(json_repr)))
                self.assertTrue(dict_compare(as_dict(json_repr), as_dict(jsonasobj_repr)))
                self.assertTrue(dict_compare(as_dict(as_dict([json_repr, json_repr])[1]),
                                             as_dict(as_dict([jsonasobj_repr, jsonasobj_repr])[0])))
                self.assertTrue(dict_compare(json.loads(as_json(json_repr)), json.loads(as_json(jsonasobj_repr))))

    def test_dict_idioms(self):
        """ Test get, setdefault, keys, and items passthroughs on dicts and jsonobjs """
        fname = os.path.join(CWD, 'input', 'meta.json')
        with open(fname) as f:
            json_repr = json.load(f)
        jsonasobj_repr = jso_load(fname)
        self.assertEqual(get(jsonasobj_repr, 'license'), get(jsonasobj_repr, 'license'))
        self.assertEqual(get(jsonasobj_repr, 'subsets')[0]['name'], get(jsonasobj_repr, 'subsets')[0].name)
        setdefault(json_repr, 'z', {"a": 17})
        setdefault(jsonasobj_repr, 'z', {"a": 17})
        self.assertEqual(json_repr['z']['a'], jsonasobj_repr.z.a)
        self.assertEqual(list(keys(json_repr)), list(keys(jsonasobj_repr)))
        self.assertEqual(list(json_repr.keys()), list(keys(jsonasobj_repr)))
        self.assertEqual(list(values(json_repr)), [as_dict(v) for v in values(jsonasobj_repr)])
        self.assertEqual(list(json_repr.values()), [as_dict(v) for v in values(jsonasobj_repr)])
        self.assertEqual(list(items(json_repr)), [(k, as_dict(v)) for k, v in items(jsonasobj_repr)])
        self.assertEqual(list(json_repr.items()), [(k, as_dict(v)) for k, v in items(jsonasobj_repr)])
        # TODO: this test should probably be finished -- we still have list of JsonObj issues
        # self.assertEqual(list(items(json_repr)),
        #                  [(k, as_json_obj(v) if isinstance(v, JsonObj) else v) for k, v in items(jsonasobj_repr)])

    def test_idempotent(self):
        """ JsonObj should be idempotent """
        o = JsonObj({"a": 42})
        self.assertEqual(id(o), id(JsonObj(o)))
        self.assertNotEqual(id(o), id(JsonObj(o, _if_missing=lambda x: (True, None))))

    def test_bool(self):
        """ Make sure the boolean operator works """
        self.assertFalse(JsonObj())
        self.assertTrue(JsonObj(a=None))
        self.assertFalse(JsonObj([]))
        self.assertTrue(JsonObj([1]))


if __name__ == '__main__':
    unittest.main()
