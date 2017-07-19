import unittest
import add_it_up as sut


class HelloworldTests(unittest.TestCase):

    def test_create_buffer_with_total(self):
        buffer_contents = ['25', '25', '25']
        expected_results = ['25', '25', '25', '=================', 'Totax: 75']
        actual_results = sut.create_buffer_with_total(buffer_contents)
        self.assertEqual(expected_results, actual_results)

