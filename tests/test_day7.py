from aoc2023.days.day7 import Day7Solver

def test_tutorial_p1():
    solver = Day7Solver('day7/tutorial.txt')
    res = solver.solve_p1()
    assert res == 6440

def test_tutorial_p2():
    solver = Day7Solver('day7/tutorial.txt')
    res = solver.solve_p2()
    assert res == 5905