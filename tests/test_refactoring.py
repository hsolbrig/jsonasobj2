import unittest
from dataclasses import dataclass

from jsonasobj import JsonObj


class Root(JsonObj):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initialized = True
        self.__post_init__()

    def __post_init__(self):
        # leave a mark saying we've been here
        self._post_initialized = True


class A(Root):
    def __init__(self, v: int) -> None:
        super().__init__()
        self.v = v


@dataclass
class C(Root):
    v: int


class InitTestCase(unittest.TestCase):
    def test_list_or_dict(self):
        """ Make sure that only lists or dictionaries get initialized """
        with self.assertRaises(TypeError) as e:
            JsonObj(17)
        self.assertIn('JSON Object can only be a list or dictionary', str(e.exception))
        o = JsonObj(JsonObj(a=1, b={"@x": 17}))
        self.assertEqual("JsonObj(a=1, b=JsonObj(**{'@x': 17}))", str(o))

    @unittest.skip("Underscore testing turns out to be far to invasive -- checks have been removed")
    def test_no_underscores(self):
        """ Make sure that underscore values cannot be constructed or added afterwards """
        with self.assertRaises(ValueError) as e:
            JsonObj(_v1=1, x=12, _y="abc")
        self.assertIn('_v1: underscore not allowed', str(e.exception))
        with self.assertRaises(ValueError) as e:
            JsonObj(dict(a="A", b="B", c=dict(c1=12), _d="D"))
        self.assertIn('_d: underscore not allowed', str(e.exception))
        with self.assertRaises(ValueError) as e:
            JsonObj(dict(a="A", b="B", c=dict(_c1=12)))
        self.assertIn("_c1: underscore not allowed", str(e.exception))
        o = JsonObj(dict(a="A", b="B", c=dict(c1=12), d="D"))
        with self.assertRaises(ValueError) as e:
            o._e = "E"
        self.assertIn("_e: underscore not allowed", str(e.exception))
        with self.assertRaises(ValueError) as e:
            o.e = dict(_f="F")
        self.assertIn("_f: underscore not allowed", str(e.exception))
        with self.assertRaises(ValueError) as e:
            o.c._g="G"
        self.assertIn("_g: underscore not allowed", str(e.exception))

    def test_basic_init(self):
        """ JsonObj __init__ function is not getting called when invoking via a dataclass """
        x = A(v=1)
        self.assertTrue(x._post_initialized)
        self.assertTrue(x._initialized)
        self.assertEqual('A(v=1)', str(x))
        y = C(1)
        self.assertTrue(y._post_initialized)
        self.assertEqual('C(v=1)', str(y))


if __name__ == '__main__':
    unittest.main()
