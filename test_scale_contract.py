"""Additional contract cases with passing controls for each tagged workflow."""

import unittest

import workflows


def scenarios(i):
    quantity, price, freight = i + 1, 800 + 37 * i, 49 + 11 * i
    day = 30 + i
    yield "quote", (quantity, price, 0 if i < 5 else freight), quantity * price + (0 if i < 5 else freight)
    overdue = [
        ((day + 1, day, 1, True), True),
        ((day, day, i + 1, True), False),
        ((day + 2, day, 0, True), False),
        ((day + 3, day, i + 1, False), False),
    ]
    yield "late", *overdue[0 if i < 5 else 1 + i % 3]
    completed = 50 + i
    on_time = completed if i % 2 else completed - 1
    pending = 0 if i < 5 else 31 + i
    yield "reliability", (on_time, completed, pending), round(100 * on_time / completed, 1)

def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    for index in range(50):
        for operation, arguments, expected in scenarios(index):
            def check(operation=operation, arguments=arguments, expected=expected):
                actual = getattr(workflows, operation)(*arguments)
                unittest.TestCase().assertEqual(actual, expected, f"{operation}{arguments!r}")

            suite.addTest(unittest.FunctionTestCase(check, description=f"{operation}_scale_{index + 1:02d}"))
    return suite
