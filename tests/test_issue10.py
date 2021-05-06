import unittest

from pyjsg.jsglib import JSGObjectMap, JSGString, JSGPattern, ArrayFactory, JSGContext, Integer
from pyjsg.validate_json import JSGPython

from json import loads as jsonloads
from jsonasobj import as_json

# Taken from
class HEX(JSGString):
    pattern = JSGPattern(r'[0-9]|[A-F]|[a-f]')


_CONTEXT = JSGContext()


class BuiltinSyntaxTestCase(unittest.TestCase):
    """ This tests a somewhat mysterious issue focused around the as_json function """
    # From: https://github.com/hsolbrig/pyjsg/blob/master/tests/test_issues/test_builtins_issue.py
    def test_1(self):
        x = JSGPython('''doc {
    v1: @string,
    v2: @number,
    v3: @int,
    v4: @bool,
    v5: @null,
    v6: @array,
    v7: @object 
}
obj {a: . , }''')

        rslt = x.conforms('''
        { "v1": "This is text!",
          "v2": -117.432e+2,
          "v3": -100173,
          "v4": false,
          "v5": null,
          "v6": [12, "text", null],
          "v7": {"q": "life", "a": 42}
        }''')
        self.assertTrue(rslt.success)

    def test_basic_map(self):
        """ Test sometimes failing pyjsg use case for jsonasobj """
        # From: https://github.com/hsolbrig/pyjsg/blob/master/tests/test_jsglib/test_objectmap.py#L15
        class IntObjectMap(JSGObjectMap):
            _name_filter = HEX
            _value_type = ArrayFactory('', _CONTEXT, Integer, 0, None)

            def __init__(self,
                         **_kwargs):
                super().__init__(_CONTEXT, **_kwargs)

        x = IntObjectMap()
        x.E = [1,2,3]
        self.assertTrue(x._is_valid())
        self.assertEqual(as_json(x), as_json(jsonloads('{"E":[1,2,3]}')))
