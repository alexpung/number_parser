import unittest
from number_parser import parse_number


#  Some test cases credit to takumakanari
#  https://github.com/takumakanari/japanese-numbers-python/blob/master/tests/test_to_arabic_parser.py


class TestNumberParse(unittest.TestCase):

    def test_kanji_only(self):
        self.assertEqual(parse_number('百八十一'), 181)
        self.assertEqual(parse_number('二百八十一'), 281)
        self.assertEqual(parse_number('千百八十一'), 1181)
        self.assertEqual(parse_number('二千百八十一'), 2181)
        self.assertEqual(parse_number('一万二千百八十一'), 12181)
        self.assertEqual(parse_number('十万二千百八十一'), 102181)
        self.assertEqual(parse_number('十一万二千百八十一'), 112181)
        self.assertEqual(parse_number('百十一万二千百八十一'), 1112181)
        self.assertEqual(parse_number('五百十一万二千百八十一'), 5112181)
        self.assertEqual(parse_number('千五百十一万二千百八十一'), 15112181)
        self.assertEqual(parse_number('四千五百十一万二千百八十一'), 45112181)
        self.assertEqual(parse_number('一億千五百十一万二千百八十一'), 115112181)
        self.assertEqual(parse_number('五十億十一'), 5000000011)
        self.assertEqual(parse_number('三百二十一億千五百十一万二千百八十一'), 32115112181)
        self.assertEqual(parse_number('千億十一'), 100000000011)
        self.assertEqual(parse_number('六千三百二十一億千五百十一万二千百八十一'), 632115112181)

    def test_decimal_mix(self):
        self.assertEqual(parse_number('0.6千株'), 600)
        self.assertEqual(parse_number('8千株'), 8000)
        self.assertEqual(parse_number('7.28千株'), 7280)
        self.assertEqual(parse_number('728千3百株'), 728300)
        self.assertAlmostEqual(parse_number('66,728.123千株'), 66728123.0)

    def test_numeric_mix(self):
        self.assertEqual(parse_number('1億1511万2181'), 115112181)
        self.assertEqual(parse_number('1000億11'), 100000000011)
        self.assertEqual(parse_number('6千3百2十1億1511万2千百8十1'), 632115112181)

    def test_zero(self):
        self.assertEqual(parse_number('一百零一'), 101)
        self.assertEqual(parse_number('三百零五'), 305)
        self.assertEqual(parse_number('一千零三十五'), 1035)
        self.assertEqual(parse_number('一千零六'), 1006)
        self.assertEqual(parse_number('三十萬零二百五十'), 300250)
        self.assertEqual(parse_number('八百萬零三百零一'), 8000301)

    def test_separator(self):
        self.assertEqual(parse_number('66,728千株'), 66728000)
        self.assertEqual(parse_number('12 566 728千株'), 12566728000)


if __name__ == '__main__':
    unittest.main()
