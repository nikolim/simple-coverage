## simple-coverage

Very basic coverage tool for educational purposes. 

### Installation
```bash 
pip install simple-coverage
```

### Usage 

Just import the package and add the @coverage decorator about functions you want to inspect.
```python
from simple_coverage.coverage import coverage

@coverage
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

If you want to use it with doctests, use the meta wrapper for the decorator.
```python
from simple_coverage.coverage import coverage, doctest_wrapper

@doctest_wrapper(coverage)
def demo(x,y) -> int:
```

### Note 
* It is currently not compatible with coverage.py or pytest since it uses the same underlying system tracer.
* It only analyses the coverage for each function call seperately.


