from aoc2023.days.day6 import Day6Solver

def test_tutorial_p1():
    solver = Day6Solver('day6/tutorial.txt')
    res = solver.solve_p1()
    assert res == 288

def test_tutorial_p2():
    solver = Day6Solver('day6/tutorial.txt')
    res = solver.solve_p2()
    assert res == 71503