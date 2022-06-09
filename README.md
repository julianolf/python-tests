# PYTHON-TESTS

![Test](https://github.com/julianolf/python-tests/actions/workflows/test.yml/badge.svg?branch=main)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

A few tests examples written in Python using the unittest framework.

## Running the tests

To run all tests in this repository execute the following command at the root directory:

```shell
$ python -m unittest discover -p "*test*.py"
```

And for a more detailed output add `-v` to the end of the command.

For a single test replace the _discovery_ argument and everything that comes afterwards with the full module path to the desired test.

```shell
$ python -m unittest ex02.test_calc.TestAdd.test_add_two_positive_numbers
```
