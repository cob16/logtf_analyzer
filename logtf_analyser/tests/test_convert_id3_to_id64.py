from unittest import TestCase

from parameterized import parameterized

from logtf_analyser.utils import convert_id3_to_id64


class TestConvert_id3_to_id64(TestCase):

    def test_convert_id3_to_id64(self):
        id64 = convert_id3_to_id64("[U:1:22202]")
        self.assertEqual(id64, 76561197960287930)

    @parameterized.expand([
        ("missing prefix", "22202]"),
        ("missing suffix", "[U:1:22202"),
    ])
    def test_rase_value_error_if(self, name, input):
        with self.assertRaises(ValueError):
            id64 = convert_id3_to_id64(input)

    def test_rase_if_not_string(self):
        with self.assertRaises(TypeError):
            convert_id3_to_id64(122434234)
            convert_id3_to_id64(True)
