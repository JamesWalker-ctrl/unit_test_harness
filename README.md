# Project Title

unit_test_harness

## Description

Script to run unit test for multiple code base (C, Python)
- Generates Pass/Fail output for each function in a predefined set
- Dynamically loads predefined test parameters from JSON

## Getting Started

### Dependencies
 TestCase class from unittest

### Executing program

* How to run the program
* Step-by-step bullets
```
% python3 -m unittest discover -v
test_add_0_python (test_harness.DynamicFunctionTests) ... ok
test_capitalize_1_python (test_harness.DynamicFunctionTests) ... ok
test_add_0_c (test_harness_c.CFunctionTests) ... ok
test_capitalize_1_c (test_harness_c.CFunctionTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.387s

OK


```

## Help

```
```

## Authors

Contributors names and contact info

james_walker2@me.com

## Version History

* 0.1
    * Initial Release
