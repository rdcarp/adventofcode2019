from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "challenges" / "data"


def _get_file_file(day: int, part_two: bool = False):
    return DATA_DIR / f"day{day:02}{'-part2' if part_two else ''}"


def get_input(day, part_two=False):
    _file = _get_file_file(day, part_two)

    return [int(s) for s in _file.open().readlines()]


def get_number_sequence(day, part_two=False):
    _file = _get_file_file(day, part_two)

    return [int(i) for i in _file.open().readline().split(",")]
