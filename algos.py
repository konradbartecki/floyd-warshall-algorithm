import itertools


class FloydAlgorithms:
    @staticmethod
    def floyd_iterative_original(distance_matrix):
        max_length = len(distance_matrix[0])
        """
        A simple implementation of Floyd's algorithm
        """
        for intermediate, start_node, end_node \
                in itertools.product \
                    (range(max_length), range(max_length), range(max_length)):
            # Assume that if start_node and end_node are the same
            # then the distance would be zero
            if start_node == end_node:
                distance_matrix[start_node][end_node] = 0
                continue
            # return all possible paths and find the minimum
            distance_matrix[start_node][end_node] = min(distance_matrix[start_node][end_node],
                                                        distance_matrix[start_node][intermediate] +
                                                        distance_matrix[intermediate][end_node])
            # Any value that have sys.maxsize has no path
        return distance_matrix

    @staticmethod
    def floyd_iterative_simple(distance_matrix):
        max_rows_length = len(distance_matrix[0])
        for intermediate in range(max_rows_length):
            for start_node in range(max_rows_length):
                for end_node in range(max_rows_length):
                    if start_node == end_node:
                        distance_matrix[start_node][end_node] = 0
                        continue
                    distance_matrix[start_node][end_node] = min(distance_matrix[start_node][end_node],
                                                                distance_matrix[start_node][intermediate] +
                                                                distance_matrix[intermediate][end_node])
        return distance_matrix

    @staticmethod
    def floyd_recursive(distance_matrix):
        def shortest_distance(start_node, end_node, intermediate):
            if start_node == end_node:
                return 0
            if intermediate == -1:
                return distance_matrix[start_node][end_node];
            a = shortest_distance(start_node, end_node, intermediate - 1)
            b = shortest_distance(start_node, intermediate, intermediate - 1)
            c = shortest_distance(intermediate, end_node, intermediate - 1)
            return min(a, b + c)

        max_length = len(distance_matrix[0])
        for i in range(max_length):
            for j in range(max_length):
                distance_matrix[i][j] = shortest_distance(i, j, max_length - 1)
        return distance_matrix

    @staticmethod
    def floyd_recursive_negative_cycle_detection(distance_matrix):
        def shortest_distance(start_node, end_node, intermediate):
            if intermediate == -1:
                return distance_matrix[start_node][end_node];
            a = shortest_distance(start_node, end_node, intermediate - 1)
            b = shortest_distance(start_node, intermediate, intermediate - 1)
            c = shortest_distance(intermediate, end_node, intermediate - 1)
            return min(a, b + c)

        max_length = len(distance_matrix[0])
        for i in range(max_length):
            for j in range(max_length):
                result = shortest_distance(i, j, max_length - 1)
                distance_matrix[i][j] = result
                if i == j and result < 0:
                    raise Exception("This graph contains negative cycles")
        return distance_matrix
