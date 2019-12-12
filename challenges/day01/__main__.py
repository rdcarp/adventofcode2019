from common.data import get_input
from common.solution import format_solution


def fuel_calc(i):
    """Part 1"""
    return int(i / 3) - 2


def fuel_calc_doubley_checked(i):
    """Part 2"""
    fuel = fuel_calc(i)

    if fuel < 0:
        return 0
    else:
        return fuel + fuel_calc_doubley_checked(fuel)


def main():
    # Provided examples.
    assert fuel_calc(12) == 2
    assert fuel_calc(14) == 2
    assert fuel_calc(1969) == 654
    assert fuel_calc(100756) == 33583

    inputs = get_input(1)

    ## Part 1
    print(format_solution(1, 1, sum(fuel_calc(i) for i in inputs)))

    ## Part 2.
    print(format_solution(1, 2, sum(fuel_calc_doubley_checked(i) for i in inputs)))


if __name__ == "__main__":
    main()
