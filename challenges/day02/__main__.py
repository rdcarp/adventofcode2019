from common.data import get_number_sequence
from common.solution import format_solution

DAY = 2

op_code_functions = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    99: lambda x, y: 1 / 0,  # lol
}


def _compute_int_code(sequence):
    i = 0

    while i * 4 <= (len(sequence) - 4):
        n = i * 4
        m = n + 4
        a, b, c, d = sequence[n:m]

        try:
            print(a, b, c)
            print(op_code_functions[a](b, c))
            print(sequence[0:4])
            sequence[d] = op_code_functions[a](b, c)
        except KeyError as err:
            print("Bad op code: %r", a)
        except ZeroDivisionError:  # lol
            break

        i += 1

    return sequence


def _tests():
    # assert _compute_int_code([int(i) for i in "1,1,1,4,99,5,6,0,99".split(",")]) == [
    #     int(i) for i in "30,1,1,4,2,5,6,0,99".split(",")
    # ]

    assert _compute_int_code([int(i) for i in "2,4,4,5,99,0".split(",")]) == [
        int(i) for i in "2,4,4,5,99,9801".split(",")
    ]
    # 


def main():
    _tests()

    input_sequence = get_number_sequence(DAY)

    # Reset state prior to fire.
    input_sequence[1] = 12
    input_sequence[2] = 2

    ans = _compute_int_code(input_sequence)[0]
    print(format_solution(DAY, 1, ans))


if __name__ == "__main__":
    main()
