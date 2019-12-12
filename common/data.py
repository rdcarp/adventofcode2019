from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "challenges" / "data"


def get_input(day, part_two=False):
    _file = DATA_DIR / f"day{day}{'-part2' if part_two else ''}"

    return [int(s) for s in _file.open().readlines()]
