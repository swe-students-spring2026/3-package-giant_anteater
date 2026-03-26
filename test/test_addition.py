import pytest
from addition_tutor.addition import align_numbers, calculate_carry, add_step_by_step, generate_random_problem, check_answer

def test_align_numbers():
    a, b = 12, 345
    aligned = align_numbers(a, b)
    assert aligned == [[0, 1, 2], [3, 4, 5]]
    assert len(aligned[0]) == len(aligned[1])
    assert all(isinstance(d, int) for row in aligned for d in row)

def test_calculate_carry():
    a, b = [1, 2, 3], [4, 5, 6]
    carry = calculate_carry(a, b)
    assert carry == [0, 0, 0]
    carry_base_5 = calculate_carry(a, b, base=5)
    assert carry_base_5 == [1, 1, 1]

def test_add_step_by_step():
    res = add_step_by_step(123, 789)
    assert res['result'] == [9, 1, 2]
    assert len(res['a_digits']) == len(res['b_digits'])
    assert all(isinstance(x, int) for x in res['carry'])

def test_generate_random_problem():
    a, b = generate_random_problem(4)
    assert len(str(a)) == 4
    assert len(str(b)) == 4

def test_check_answer():
    assert check_answer(10, 10)
    assert not check_answer(5, 6)