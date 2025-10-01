##
## test_harness_c.py
## v0.1.0
##
## Script dynamically loads predefined test parameters from test_functions.json
## Unit test all functions using command,
##  $ python3 -m unittest discover -v
##

import json
import importlib
import unittest
import ctypes

def load_test_cases(path):
    with open(path) as f:
        return [c for c in json.load(f) if c["language"] == "c"]

def make_test(case):
    def test(self):
        lib = ctypes.CDLL(case["library"])
        func = getattr(lib, case["function"])
        if case["function"] == "capitalize":
            input_str = case["args"][0].encode()
            output = ctypes.create_string_buffer(len(input_str) + 1)
            func.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
            func(input_str, output)
            result = output.value.decode()
        else:
            func.argtypes = [ctypes.c_int] * len(case["args"])
            func.restype = ctypes.c_int
            result = func(*case["args"])
        self.assertEqual(result, case["expected"])
    return test

class CFunctionTests(unittest.TestCase): pass

for i, case in enumerate(load_test_cases("test_functions.json")):
    test_name = f"test_{case['function']}_{i}_{case['language']}"
    test_method = make_test(case)
    setattr(CFunctionTests, test_name, test_method)
