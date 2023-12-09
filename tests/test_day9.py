from aoc2023.days.day9 import Day9Solver

def test_tutorial_p1():
    solver = Day9Solver('day9/tutorial.txt')
    res = solver.solve_p1()
    assert res == 114

def test_tutorial_p2():
    solver = Day9Solver('day9/tutorial.txt')
    res = solver.solve_p2()
    assert res == 2
