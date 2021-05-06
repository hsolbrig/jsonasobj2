import unittest
from typing import Optional

from jsonasobj import JsonObj, as_json


class MyObj(JsonObj):
   def __init__(self, a: JsonObj):
       super().__init__()
       self.a = a


class RecursiveObject(JsonObj):
    def __init__(self, parent: Optional["RecursiveObject"] = None):
        super().__init__()
        self.parent = parent

class RecursiveObject2(JsonObj):
    _idempotent = False
    def __init__(self, parent: Optional["RecursiveObject"] = None):
        super().__init__()
        self.parent = parent


class DangerousConstructor(unittest.TestCase):
    def test_unintended_recursion(self):
        o1 = JsonObj(x=1)
        o2 = MyObj(o1)
        self.assertNotEqual(id(o1), id(o2))

    def test_deliberate_recursion(self):
        grandfather = RecursiveObject()
        father = RecursiveObject(grandfather)
        me = RecursiveObject(father)
        self.assertEqual(id(me), id(me.parent))

        grandfather = RecursiveObject2()
        father = RecursiveObject2(grandfather)
        me = RecursiveObject2(father)
        self.assertNotEqual(id(me), id(me.parent))

if __name__ == '__main__':
    unittest.main()
