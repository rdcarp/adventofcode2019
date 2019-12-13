from common.data import get_number_sequence
from common.solution import format_solution
from itertools import product

DAY = 2

op_code_functions = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
    99: lambda x, y: 1 / 0,  # lol
}


def _compute_int_code(sequence, noun, verb):
    sequence[1] = noun
    sequence[2] = verb
    i = 0
    while i * 4 <= (len(sequence) - 4):
        n = i * 4
        m = n + 4
        a, b, c, d = sequence[n:m]

        try:
            sequence[d] = op_code_functions[a](sequence[b], sequence[c])
        except ZeroDivisionError:  # lol
            break

        i += 1

    return sequence


def _part_2(sequence, target=19690720):
    for noun, verb in product(range(100), range(100)):
        seq = sequence.copy()
        try:
            if _compute_int_code(seq, noun, verb)[0] == target:
                return 100 * noun + verb
        except KeyError:
            pass

    raise RuntimeError("Target not found")


def main():
    input_sequence = get_number_sequence(DAY)

    day_1_sequence = input_sequence.copy()
    ans = _compute_int_code(day_1_sequence, 12, 2)[0]
    print(format_solution(DAY, 1, ans))

    ans_2 = _part_2(input_sequence)
    print(format_solution(DAY, 2, ans_2))


if __name__ == "__main__":
    main()
