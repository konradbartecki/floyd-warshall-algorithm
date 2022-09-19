import copy
import timeit

from main import FloydAlgorithms
from test_data import (test_configuration_big_graphs)


def time_profiling():
    test_number = 10
    for input_graph in test_configuration_big_graphs:
        print("====")
        print("n =", len(input_graph[0]))
        print("Iterative_Original:",
              timeit.timeit(lambda: FloydAlgorithms.floyd_iterative_original(copy.deepcopy(input_graph)),
                            number=test_number))
        print("Iterative_Simple:",
              timeit.timeit(lambda: FloydAlgorithms.floyd_iterative_simple(copy.deepcopy(input_graph)),
                            number=test_number))
        print("Recursive:", timeit.timeit(lambda: FloydAlgorithms.floyd_recursive(copy.deepcopy(input_graph)),
                                          number=test_number))
        print("Recursive_WithNegativeDetection:",
              timeit.timeit(lambda: FloydAlgorithms
                            .floyd_recursive_negative_cycle_detection(copy.deepcopy(input_graph)), number=test_number))


time_profiling()
