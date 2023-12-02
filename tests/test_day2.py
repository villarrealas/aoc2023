from aoc2023.days.day2 import GameChecker

def test_tutorial_p1():
    gamechecker = GameChecker('day2/tutorial1.txt')
    res = gamechecker.solve(12,13,14)
    assert res == 8

def test_tutorial_p2():
    gamechecker = GameChecker('day2/tutorial1.txt')
    res = gamechecker.find_power()
    assert res == 2286