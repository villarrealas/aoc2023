from aoc2023.days.day5 import Day5Solver

def test_tutorial_p1():
    solver = Day5Solver('day5/tutorial.txt')
    res = solver.solve()
    assert res == 35

def test_tutorial_p2():
    solver = Day5Solver('day5/tutorial.txt')
    res = solver.solve_reverse()
    assert res == 46