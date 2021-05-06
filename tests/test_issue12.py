import json
import unittest

from jsonasobj import JsonObj, as_json


class ShapeAssociation(JsonObj):
    def __init__(self,
                 nodeSelector, shapeLabel,
                 status=None, reason=None,
                 appinfo=None) -> None:

        self.nodeSelector = nodeSelector
        self.shapeLabel = shapeLabel
        self.status = status if status is not None else "C",
        self.reason = reason
        self.appinfo = appinfo
        super().__init__()


expected = {
   "nodeSelector": "http://example.org/people/42",
   "shapeLabel": "http://example.org/model/Person",
   "status": [
      "C"
   ],
   "reason": "cause",
   "appinfo": None
}


class PositionalTestCase(unittest.TestCase):
    def test_positional(self):
        """ jsonasobj has to support positional constructors """
        s = ShapeAssociation("http://example.org/people/42", 'http://example.org/model/Person', reason='cause')
        self.assertEqual(expected, json.loads(as_json(s)))


if __name__ == '__main__':
    unittest.main()
