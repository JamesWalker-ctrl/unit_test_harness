##
## test_harness.py
## v0.1.0
##
## Script dynamically loads predefined test parameters from test_functions.json
## Unit test all functions using command,
##  $ python3 -m unittest discover -v
##

import json
import importlib
import unittest

def load_function(module_name, function_name):
    module = importlib.import_module(module_name)
    return getattr(module, function_name)

def load_test_cases(path):
    with open(path) as f:
        return [case for case in json.load(f) if case["language"] == "python"]

def make_test(case):
    def test(self):
        func = load_function(case["module"], case["function"])
        result = func(*case["args"])
        self.assertEqual(result, case["expected"])
    return test

# Dynamically create a test class
class DynamicFunctionTests(unittest.TestCase):
    pass

# Attach each test case as a method
for i, case in enumerate(load_test_cases("test_functions.json")):
    test_name = f"test_{case['function']}_{i}_{case['language']}"
    test_method = make_test(case)
    setattr(DynamicFunctionTests, test_name, test_method)
