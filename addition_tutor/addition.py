import random

def align_numbers(a: int, b: int, fill: int = 0):
    """Aligns two integers by digits, padding the shorter number with `fill`."""
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]
    max_len = max(len(a_digits), len(b_digits))
    a_digits = [fill]*(max_len - len(a_digits)) + a_digits
    b_digits = [fill]*(max_len - len(b_digits)) + b_digits
    return [a_digits, b_digits]

def calculate_carry(a_digits, b_digits, base: int = 10):
    """Calculates carry for column addition."""
    carry = 0
    carry_list = []
    for ad, bd in zip(reversed(a_digits), reversed(b_digits)):
        total = ad + bd + carry
        carry = total // base
        carry_list.append(carry)
    return list(reversed(carry_list))

def add_step_by_step(a: int, b: int, show_carry: bool = True):
    """Adds two integers step-by-step, showing digits, carry, and result."""
    a_digits, b_digits = align_numbers(a, b)
    carry = calculate_carry(a_digits, b_digits) if show_carry else [0]*len(a_digits)
    result_digits = []
    c = 0
    for ad, bd, cv in zip(reversed(a_digits), reversed(b_digits), reversed(carry)):
        s = ad + bd + c
        result_digits.append(s % 10)
        c = s // 10
    if c > 0:
        result_digits.append(c)
    result_digits.reverse()
    return {
        "a_digits": a_digits,
        "b_digits": b_digits,
        "carry": carry,
        "result": result_digits
    }

def format_steps(step_dict, style: str = "plain"):
    """Pretty-print addition steps."""
    a_str = " ".join(map(str, step_dict["a_digits"]))
    b_str = " ".join(map(str, step_dict["b_digits"]))
    carry_str = " ".join(map(str, step_dict["carry"]))
    result_str = " ".join(map(str, step_dict["result"]))
    return f"Carry: {carry_str}\n  {a_str}\n+ {b_str}\n= {result_str}"

def generate_random_problem(num_digits: int = 5):
    """Generates two random integers with `num_digits` digits."""
    a = random.randint(10**(num_digits-1), 10**num_digits - 1)
    b = random.randint(10**(num_digits-1), 10**num_digits - 1)
    return a, b

def check_answer(user_input: int, correct_sum: int) -> bool:
    """Validates user's answer."""
    return user_input == correct_sum