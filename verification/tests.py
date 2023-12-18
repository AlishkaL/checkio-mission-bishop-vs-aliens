"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


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
            "input": [3, 2, 5, 4, [(2, 2), (1, 4)]],
            "answer": True,
        },
    ]
}
