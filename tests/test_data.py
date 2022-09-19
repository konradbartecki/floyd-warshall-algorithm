INF = 9999

graph1_input = [
    [0, 7, INF, 8],
    [INF, 0, 5, INF],
    [INF, INF, 0, 2],
    [INF, INF, INF, 0]
]
graph1_expected = \
    [[0, 7, 12, 8],
     [INF, 0, 5, 7],
     [INF, INF, 0, 2],
     [INF, INF, INF, 0]]

graph2_input = [[0, 5, INF, 10],
                [INF, 0, 3, INF],
                [INF, INF, 0, 1],
                [INF, INF, INF, 0]
                ]
graph2_expected = [[0, 5, 8, 9],
                   [INF, 0, 3, 4],
                   [INF, INF, 0, 1],
                   [INF, INF, INF, 0]]

graph3_input = [[0, INF, -2, INF],
                [4, 0, 3, INF],
                [INF, INF, 0, 2],
                [INF, -1, INF, 0]
                ]
graph3_expected = [[0, -1, -2, 0],
                   [4, 0, 2, 4],
                   [5, 1, 0, 2],
                   [3, -1, 1, 0]]

graph_big_n6 = [[0, 6, 9, 5, 8, 3], [8, 0, 3, 1, 5, 2], [3, INF, 0, 1, 9, 8], [3, 7, 1, 0, 7, 2], [9, 4, 3, 9, 0, 5],
              [3, 3, 4, 7, 7, 0]]

graph_big_n7 = [[0, 4, INF, 5, 9, 7, 4], [8, 0, 1, 8, 8, 9, 6], [7, 2, 0, 1, INF, INF, 6], [5, 7, 6, 0, 6, 3, 4],
              [4, INF, INF, 4, 0, INF, 2], [7, INF, 3, 9, 7, 0, 1], [3, 5, 9, 5, 6, INF, 0]]

graph_big_n8 = [[0, 7, 6, 7, INF, 6, 9, 8], [INF, 0, 3, 5, 4, 8, INF, 4], [1, 7, 0, 9, 6, 7, 1, 3],
              [2, INF, 3, 0, 6, 7, 8, 6], [7, INF, 4, 6, 0, 9, 3, 1], [3, 1, 9, 9, 6, 0, 7, 4],
              [INF, 3, 4, 6, 3, 8, 0, INF], [6, 9, 4, 9, 3, 9, 7, 0]]

test_configuration = [
    (graph1_input, graph1_expected),
    (graph2_input, graph2_expected),
    (graph3_input, graph3_expected)
]

test_configuration_big_graphs = [
    graph_big_n6, graph_big_n7, graph_big_n8
]
