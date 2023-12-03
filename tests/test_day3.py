from aoc2023.days.day3 import Day3Solver

def test_tutorial_p1():
    solver = Day3Solver('day3/tutorial1.txt')
    res = solver.solve()
    assert res == 4361

def test_tutorial_p2():
    solver = Day3Solver('day3/tutorial1.txt')
    res = solver.solve_gr()
    assert res == 467835