from aoc2023.days.day10 import Day10Solver

def test_tutorial_p1():
    solver = Day10Solver('day10/tutorial1.txt')
    res = solver.solve_p1()
    assert res == 4

    solver = Day10Solver('day10/tutorial2.txt')
    res = solver.solve_p1()
    assert res == 8

#def test_tutorial_p2():
#    solver = Day10Solver('day10/tutorial.txt')
#    res = solver.solve_p2()
#    assert res == 2
