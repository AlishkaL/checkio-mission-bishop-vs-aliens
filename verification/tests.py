"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
from random import randint


def solution(x: int, y: int, w: int, h: int, aliens: list[tuple[int, int]]) -> bool:
    exits = [(ex, ey) for ex in (0, w - 1) for ey in (0, h - 1)]
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        way = [[x, y]]
        if 0 <= x + dx < w and 0 <= y + dy < h:
            mx, my = x, y
            while True:
                mx += dx
                my += dy
                way.append([mx, my])
                if (mx, my) in aliens + [(x, y)]:
                    break
                if (mx, my) in exits:
                    return True
                if my in (0, h - 1):
                    dy *= -1
                if mx in (0, w - 1):
                    dx *= -1
    return False


def make_random_tests(num: int) -> list[dict]:
    random_tests = []
    for _ in range(num):
        width = randint(4, 12)
        height = randint(4, 12)
        aliens_num = randint(0, 4)
        aliens = list({(randint(0, width - 1), randint(0, height - 1)) for _ in range(aliens_num)})
        while True:
            start = (randint(0, width - 1), randint(0, height - 1))
            if start not in ((0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1), *aliens):
                break
        inputs = (*start, width, height, aliens)
        random_tests.append({"input": [*inputs], "answer": solution(*inputs)})
    return random_tests


TESTS = {
    "Basics": [
        {
            "input": [0, 2, 5, 5, []],
            "answer": False,
        },
        {
            "input": [4, 4, 9, 9, [(0, 0), (0, 8), (8, 0), (8, 8)]],
            "answer": False,
        },
        {
            "input": [1, 1, 1000, 2, [(0, 0), (0, 1), (999, 0)]],
            "answer": True,
        },
    ],
    "Extra": [
        {
            "input": [1, 1, 1000, 2, [(0, 0), (0, 1), (999, 1)]],
            "answer": False,
        },
        {
            "input": [3, 2, 4, 4, [(1, 2), (0, 1)]],
            "answer": False,
        },
        {
            "input": [3, 2, 4, 5, [(2, 2), (1, 4)]],
            "answer": True,
        },
        {
            "input": [0, 2, 10, 5, []],
            "answer": True,
        },
        {
            "input": [4, 2, 10, 5, [(2, 2)]],
            "answer": False,
        },
    ],
    "Randoms": list(make_random_tests(10)),
}
