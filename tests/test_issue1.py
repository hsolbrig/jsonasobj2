
import unittest


class ByteArrayTestCase(unittest.TestCase):
    def test_bytearray(self):
        from jsonasobj import load
        load("http://hl7.org/fhir/R4/patient-example-f201-roel.json")


if __name__ == '__main__':
    unittest.main()
