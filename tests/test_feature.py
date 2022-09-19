import unittest
from parameterized import parameterized
from main import FloydAlgorithms
from test_data import (test_configuration)
import copy


class UnitTests(unittest.TestCase):

    @parameterized.expand(test_configuration)
    def test_iterative_original(self, weighted_graph, expected):
        actual_result = FloydAlgorithms.floyd_iterative_original(copy.deepcopy(weighted_graph))
        self.assertEqual(expected, actual_result)

    @parameterized.expand(test_configuration)
    def test_iterative_simple(self, weighted_graph, expected):
        actual_result = FloydAlgorithms.floyd_iterative_simple(copy.deepcopy(weighted_graph))
        self.assertEqual(expected, actual_result)

    @parameterized.expand(test_configuration)
    def test_recursive_negative_cycle_detection_success(self, weighted_graph, expected):
        actual_result = FloydAlgorithms.floyd_recursive_negative_cycle_detection(copy.deepcopy(weighted_graph))
        self.assertEqual(expected, actual_result)

    @parameterized.expand(test_configuration)
    def test_recursive(self, weighted_graph, expected):
        actual_result = FloydAlgorithms.floyd_recursive(copy.deepcopy(weighted_graph))
        self.assertEqual(expected, actual_result)

    def test_recursive_negative_cycle_detection_throws(self):
        weighted_graph = [
            [0, 1, 1],
            [1, 2, -1],
            [2, 3, -1],
             [3, 0, -1]
        ]
        with self.assertRaises(Exception) as ex:
            FloydAlgorithms.floyd_recursive_negative_cycle_detection(copy.deepcopy(weighted_graph))
        self.assertEqual(ex.exception.args[0], "This graph contains negative cycles")

if __name__ == '__main__':
    unittest.main()
