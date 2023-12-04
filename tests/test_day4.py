from aoc2023.days.day4 import Day4Solver

def test_tutorial_p1():
    solver = Day4Solver('day4/tutorial.txt')
    res = solver.solve()
    assert res == 13

def test_tutorial_p2():
    solver = Day4Solver('day4/tutorial.txt')
    res = solver.solve_scratchers()
    assert res == 30