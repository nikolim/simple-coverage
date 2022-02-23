## simple-coverage

Very basic coverage tool for educational purposes. 

### Installation
```bash 
pip install simple-coverage
```

### Usage 

Just import the package and add the @print_coverage decorator above functions you want to inspect.
```python
from simple_coverage.coverage import coverage

@print_coverage
def demo(x, y) -> int:
    """
    Demo function
    """
	product = x * y 
	if product < 10:
		return product * 2
	else: 
	return product

if __name__ == "__main__":
	demo(3,5)
```

When simply runnning the Python-file, this will create the following output:
```bash
Function: demo(3, 5)

CALLED line 9:      product = x * y
CALLED line 10:     if product < 10:
MISSED line 11:         return product * 2
IGNORE line 12:     else:
CALLED line 13:         return product

Instruction coverage: 75.0 %
Branch coverage: 50.0 %
```
### Doctests

If you want to use it with doctests, use the meta wrapper `@doctest_wrapper` and the `log_coverage` decorator. This will create a `simple-coverage.json` file in the current working directory since writing into the console would collide with the doctests.
```python
from simple_coverage.coverage import log_coverage, doctest_wrapper

@doctest_wrapper(log_coverage)
def demo(x,y) -> int:
	...
```
Look at the `demo.py` file for reference. To start the doctest use pytest as usual.
```bash
pytest --doctest-modules demo.py
```
Afterwards you can create the report:
```bash
python3 -m simple_coverage.report
```
Note that all runs will be saved for the next report. To start over and delete to report run:
```bash
python3 -m simple_coverage.clean
```