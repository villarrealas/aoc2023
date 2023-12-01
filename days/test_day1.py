from .day1 import Calibration

def test_tutorial_p1():
    calibration = Calibration('inputs/day1/tutorial1.txt')
    res = calibration.value(allow_strings=False)
    assert res == 142

def test_tutorial_p2():
    calibration = Calibration('inputs/day1/tutorial2.txt')
    res = calibration.value(allow_strings=True)
    assert res == 281