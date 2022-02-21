from simple_coverage.coverage import print_coverage, log_coverage, doctest_wrapper


@print_coverage
def demo(x, y) -> bool:
	"""
	Demo function which prints output to console
	"""
	product = x * y
	if product < 10:
		return product * 2
	else:
		return product


@doctest_wrapper(log_coverage)
def demo_2(x, y) -> bool:
	"""
	Demo function which writes output to file
	>>> demo_2(3, 5)
	16 
	"""
	sum = x + y
	if sum < 100:
		sum = sum * 2
	elif sum < 50:
		sum = sum * 3
	else:
		sum = sum * 4
	return sum


if __name__ == "__main__":
	demo(3, 5)
	demo_2(10, 5)
