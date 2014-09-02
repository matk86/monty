__author__ = 'Shyue Ping Ong'
__copyright__ = 'Copyright 2014, The Materials Virtual Lab'
__version__ = '0.1'
__maintainer__ = 'Shyue Ping Ong'
__email__ = 'ongsp@ucsd.edu'
__date__ = '1/24/14'


import unittest
import numpy as np
import json
import datetime

from monty.json import MSONable, MSONError, MontyEncoder, MontyDecoder


class MSONableTest(unittest.TestCase):

    def setUp(self):
        class GoodMSONClass(MSONable):

            def __init__(self, a, b):
                self.a = a
                self.b = b

            def to_dict(self):
                d = {'a': self.a, 'b': self.b}
                return d

            @classmethod
            def from_dict(cls, d):
                return GoodMSONClass(d['a'], d['b'])

        self.good_cls = GoodMSONClass

        class BadMSONClass(MSONable):

            def __init__(self, a, b):
                self.a = a
                self.b = b

            def to_dict(self):
                d = {'a': self.a, 'b': self.b}
                return d

        self.bad_cls = BadMSONClass

    def test_to_from_dict(self):
        obj = self.good_cls("Hello", "World")
        d = obj.to_dict()
        self.assertIsNotNone(d)
        self.good_cls.from_dict(d)
        obj = self.bad_cls("Hello", "World")
        d = obj.to_dict()
        self.assertIsNotNone(d)
        self.assertRaises(MSONError, self.bad_cls.from_dict, d)

    def test_to_json(self):
        obj = self.good_cls("Hello", "World")
        self.assertIsNotNone(obj.to_json)


class JsonTest(unittest.TestCase):

    def test_datetime(self):
        dt = datetime.datetime.now()
        jsonstr = json.dumps(dt, cls=MontyEncoder)
        d = json.loads(jsonstr, cls=MontyDecoder)
        self.assertEqual(type(d), datetime.datetime)
        self.assertEqual(dt, d)
        #Test a nested datetime.
        a = {'dt': dt, "a": 1}
        jsonstr = json.dumps(a, cls=MontyEncoder)
        d = json.loads(jsonstr, cls=MontyDecoder)
        self.assertEqual(type(d["dt"]), datetime.datetime)

    def test_numpy(self):
        x = np.array([1, 2, 3])
        self.assertRaises(TypeError, json.dumps, x)
        djson = json.dumps(x, cls=MontyEncoder)
        d = json.loads(djson)
        self.assertEqual(d["@class"], "array")
        self.assertEqual(d["@module"], "numpy")
        self.assertEqual(d["data"], [1, 2, 3])
        x = json.loads(djson, cls=MontyDecoder)
        self.assertEqual(type(x), np.ndarray)
        x = np.min([1, 2, 3]) > 2
        self.assertRaises(TypeError, json.dumps, x)



if __name__ == "__main__":
    unittest.main()
