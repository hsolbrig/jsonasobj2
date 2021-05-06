
import unittest

import os

from jsonasobj import JsonObj


class LoadTestCase(unittest.TestCase):
    def test_load_file(self):
        from jsonasobj import load
        json_fname = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'file.json')
        json_obj = load(json_fname)
        self.assertEqual([1, False, -12.7, "qwert"], json_obj.a_dict.vals)

    def test_load_uri(self):
        from jsonasobj import load
        # A relatively stable JSON file
        json_obj = load("http://hl7.org/fhir/STU3/account-example.json")
        self.assertEqual('Coverage/7546D', json_obj.coverage[0].coverage.reference)

    def test_load_fp(self):
        from jsonasobj import load
        json_fname = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'file.json')
        with open(json_fname) as f:
            json_obj = load(f)
        self.assertEqual([1, False, -12.7, "qwert"], json_obj.a_dict.vals)

    def test_bad_load(self):
        from jsonasobj import load
        json_fname = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'filex.json')
        with self.assertRaises(FileNotFoundError):
            json_obj = load(json_fname)
        self.assertEqual(JsonObj(), load(dict()))


    @unittest.skipIf(True, "FHIR servers no longer appear to do redirects (correctly)")
    def test_load_redirect(self):
        from jsonasobj import load
        json_obj = load("http://hl7.org/fhir/Patient/f001")
        self.assertEqual('male', json_obj.gender)

if __name__ == '__main__':
    unittest.main()
