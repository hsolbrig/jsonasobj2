
import unittest
import jsonasobj


class ExtendedNamespaceTestCase(unittest.TestCase):
    """ ExtendedNamespace is a dictionary / namespace combination.  Any valid python identifiers are also available
    as first class members.
    """
    def test_extendednamespace(self) -> None:
        # Direct constructor
        ens = jsonasobj.ExtendedNamespace(i1=1, i2='a', i3='17')
        # Test dictionary and namespace behavior
        self.assertEqual(1, ens.i1)
        self.assertEqual('a', ens.i2)
        self.assertEqual('17', ens.i3)
        self.assertEqual(3, len(ens))
        self.assertTrue('i1' in ens)
        self.assertFalse('i4' in ens)
        del ens['i1']
        self.assertEqual(2, len(ens))
        self.assertFalse('i1' in ens)
        ens.i4 = 243
        self.assertEqual(243, ens.i4)
        self.assertEqual(243, ens['i4'])

        # Construct from a dictionary, using common json-ld idioms
        ens1 = jsonasobj.ExtendedNamespace(**{'i1': 1, '@foo': "bar", 'x:y': ens})
        self.assertEqual(1, ens1.i1)
        self.assertEqual('bar', ens1['@foo'])
        self.assertEqual(ens, ens1['x:y'])
        self.assertEqual(3, len(ens1))

    def test_extended_access(self) -> None:
        ens = jsonasobj.ExtendedNamespace(i1=1, i2='a', i3='17')
        self.assertEqual("no", ens._get('i4', 'no'))


if __name__ == '__main__':
    unittest.main()
