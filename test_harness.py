
##class TryTesting(TestCase):
##    def test_always_passes(self):
##        self.assertTrue(True)
##
##    def test_always_fails(self):
##        self.assertTrue(False)

##import json
##import importlib
##from unittest import TestCase

##def load_function(module_name, function_name):
##    module = importlib.import_module(module_name)
##    return getattr(module, function_name)

##def load_test_cases(json_path):
##    with open(json_path, 'r') as f:
##        return json.load(f)

##class DynamicFunctionTests(TestCase):
##    def test_predefined_functions(self):
##        test_cases = load_test_cases("test_functions.json")
##        for case in test_cases:
##            func = load_function(case["module"], case["function"])
##            with self.subTest(func=case["function"]):
##                result = func(*case["args"])
##                self.assertEqual(result, case["expected"])


import json
import importlib
import unittest

def load_function(module_name, function_name):
    module = importlib.import_module(module_name)
    return getattr(module, function_name)

def load_test_cases(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

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
    test_name = f"test_{case['function']}_{i}"
    test_method = make_test(case)
    setattr(DynamicFunctionTests, test_name, test_method)



