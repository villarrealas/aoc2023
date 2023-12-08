from aoc2023.days.day8 import Day8Solver

def test_tutorial_p1():
    solver = Day8Solver('day8/tutorial1.txt')
    res = solver.solve_p1()
    assert res == 2

    solver = Day8Solver('day8/tutorial2.txt')
    res = solver.solve_p2()

def test_tutorial_p2():
    solver = Day8Solver('day8/tutorial3.txt')
    res = solver.solve_p2()
    assert res == 6

def test_tutorial_p2_alt():
    solver = Day8Solver('day8/tutorial3.txt')
    res = solver.solve_p2_alt()
    assert res == 6

def test_tutorial_p2_mt():
    solver = Day8Solver('day8/tutorial3.txt')
    res = solver.solve_p2_mt()
    assert res == 6

def test_tutorial_p2_lcm():
    solver = Day8Solver('day8/tutorial3.txt')
    res = solver.solve_p2_lcm()
    assert res == 6