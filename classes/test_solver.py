from solver import SolverBase
import pytest

def test_read():
    '''test the read functionality'''
    path_to_file = 'inputs/tests/test1.txt'
    tester = SolverBase(path_to_file)
    tester.store_input()
    assert tester.stored_lines == ['sierralikessimpletestcases']

def test_value():
    '''test that error is raised correctly'''
    path_to_file = 'inputs/tests/test1.txt'
    tester = SolverBase(path_to_file)
    with pytest.raises(NotImplementedError):
        tester.value()