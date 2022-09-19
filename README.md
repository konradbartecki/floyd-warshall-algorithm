# Floyd-warshall-algorithm

[![Python application](https://github.com/konradbartecki/floyd-warshall-algorithm/actions/workflows/python-app.yml/badge.svg)](https://github.com/konradbartecki/floyd-warshall-algorithm/actions/workflows/python-app.yml)


## Unit tests

```
============================= test session starts ==============================
collecting ... collected 13 items

tests/test_feature.py::UnitTests::test_iterative_original_0 PASSED       [  7%]
tests/test_feature.py::UnitTests::test_iterative_original_1 PASSED       [ 15%]
tests/test_feature.py::UnitTests::test_iterative_original_2 PASSED       [ 23%]
tests/test_feature.py::UnitTests::test_iterative_simple_0 PASSED         [ 30%]
tests/test_feature.py::UnitTests::test_iterative_simple_1 PASSED         [ 38%]
tests/test_feature.py::UnitTests::test_iterative_simple_2 PASSED         [ 46%]
tests/test_feature.py::UnitTests::test_recursive_0 PASSED                [ 53%]
tests/test_feature.py::UnitTests::test_recursive_1 PASSED                [ 61%]
tests/test_feature.py::UnitTests::test_recursive_2 PASSED                [ 69%]
tests/test_feature.py::UnitTests::test_recursive_negative_cycle_detection_success_0 PASSED [ 76%]
tests/test_feature.py::UnitTests::test_recursive_negative_cycle_detection_success_1 PASSED [ 84%]
tests/test_feature.py::UnitTests::test_recursive_negative_cycle_detection_success_2 PASSED [ 92%]
tests/test_feature.py::UnitTests::test_recursive_negative_cycle_detection_throws PASSED [100%]

============================== 13 passed in 2.58s ==============================
```

## Performance tests

```
runs = 10

====
n = 6
Iterative_Original: 0.0009580010082572699
Iterative_Simple: 0.00085936498362571
Recursive: 0.04821641597663984
Recursive_WithNegativeDetection: 0.06591107603162527
====
n = 7
Iterative_Original: 0.00131764798425138
Iterative_Simple: 0.001207950001116842
Recursive: 0.1840702180052176
Recursive_WithNegativeDetection: 0.26733793900348246
====
n = 8
Iterative_Original: 0.0016334149986505508
Iterative_Simple: 0.001711071003228426
Recursive: 0.7366994370240718
Recursive_WithNegativeDetection: 1.0139947880525142
```


## Test data generation

Excel function

`=IF(ROW()=COLUMN(); 0; IF(RAND()>0,9;"INF";RANDBETWEEN(1; 9)))`

then to collect data, for each excel row

`="["&TEXTJOIN(",";TRUE;A1:O1)&"]"`

then to sum rows

`="["&TEXTJOIN(","; TRUE; R1:R15)&"]"`
