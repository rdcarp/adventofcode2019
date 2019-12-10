def fuel_calc(i):
    """Part 1"""
    return int(i / 3) - 2


if __name__ == "__main__":
    # Provided examples.
    assert fuel_calc(12) == 2
    assert fuel_calc(14) == 2
    assert fuel_calc(1969) == 654
    assert fuel_calc(100756) == 33583

    # YOLO file path.
    inputs = [int(s) for s in open("input").readlines()]

    print(sum(fuel_calc(i) for i in inputs))
