import json
import unittest

import jsonasobj
from jsonasobj import JsonObj

test_data = {
    "name": "Markus Lanthaler"
}
test_json = str(test_data).replace("'", '"')


class TestObj(JsonObj):
    def _default(self, obj):
        return super()._default(obj)


class NonDefaultTestCase(unittest.TestCase):
    def test_old_default(self):
        e = TestObj(**json.loads(test_json))
        # Failure point 1
        self.assertEqual('''{
   "name": "Markus Lanthaler"
}''', jsonasobj.as_json(e))
        self.assertEqual('''{
yy"name": "Markus Lanthaler"
}''', jsonasobj.as_json(e, indent='yy'))
        # Failure point 2
        self.assertEqual('''{
   "name": "Markus Lanthaler"
}''', e._as_json_dumps())
        self.assertEqual('''{
zz"name": "Markus Lanthaler"
}''', e._as_json_dumps(indent='zz'))


if __name__ == '__main__':
    unittest.main()
