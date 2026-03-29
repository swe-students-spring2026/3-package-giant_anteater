import pytest
from anteater_tools.addition_tutor.addition import align_numbers, calculate_carry, add_step_by_step

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
    a, b = [1, 2, 3], [9, 8, 7]
    carry = calculate_carry(a, b)
    assert carry == [1, 1, 1]


def test_add_step_by_step():
    res = add_step_by_step(123, 789)
    assert res['result'] == [9, 1, 2]
    assert len(res['a_digits']) == len(res['b_digits'])
    assert all(isinstance(x, int) for x in res['carry'])
# test_align_numbers()
# print("✅ test_align_numbers passed!")
# test_calculate_carry()
# print("✅ test_calculate_carry passed!")
# test_add_step_by_step()
# print("✅ test_add_step_by_step passed!")
# print("\n✨ All tests passed successfully!")
