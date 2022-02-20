from simple_coverage.coverage import coverage


@coverage
def demo(x, y) -> bool:
    """
    Demo function
    """
    product = x * y
    if product < 10:
        return product * 2
    else:
        return product


if __name__ == "__main__":
    demo(3, 5)
