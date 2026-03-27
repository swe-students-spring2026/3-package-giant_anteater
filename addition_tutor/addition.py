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
    """
    Adds two integers step-by-step, showing digits, carry, result, 
    and also generates textual explanations for each column.
    """
    a_digits, b_digits = align_numbers(a, b)
    carry = calculate_carry(a_digits, b_digits) if show_carry else [0]*len(a_digits)
    result_digits = []
    c = 0
    explanations = []

    # Process each column from right to left
    for i, (ad, bd, cv) in enumerate(zip(reversed(a_digits), reversed(b_digits), reversed(carry))):
        s = ad + bd + c
        digit_result = s % 10
        result_digits.append(digit_result)
        explanations.append(
            f"Column {1+i}: {ad} + {bd} + previous carry {c} = {s}, "
            f"write {digit_result}, carry {s // 10}"
        )
        c = s // 10

    # Handle final leftmost carry
    if c > 0:
        result_digits.append(c)
        explanations.append(f"Final carry {c} is added as the leftmost digit.")

    result_digits.reverse()
    # explanations.reverse()  # make steps from left to right

    return {
        "a_digits": a_digits,
        "b_digits": b_digits,
        "carry": carry,
        "result": result_digits,
        "explanations": explanations
    }
def format_steps(step_dict):
    """
    Pretty-print addition steps with:
    - Digits aligned in columns
    - Carry row BELOW the plus sign, right under each digit
    - Result at the bottom
    """
    a_digits = step_dict["a_digits"]
    b_digits = step_dict["b_digits"]
    carry = step_dict["carry"]
    result = step_dict["result"]
    explanations = step_dict.get("explanations", [])
    a_show = "".join(map(str, a_digits))
    b_show = "".join(map(str, b_digits))
    carry_show = "".join(map(str, carry))
    result_show = "".join(map(str, result))

    # Make all lists the same length
    max_len = max(len(a_digits), len(b_digits), len(result))
    a_digits = [0]*(max_len - len(a_digits)) + a_digits
    b_digits = [0]*(max_len - len(b_digits)) + b_digits
    carry = (carry + [0])[-max_len:]
    result = [0]*(max_len - len(result)) + result

    # Convert digits to strings
    a_str = " ".join(map(str, a_digits))
    b_str = " ".join(map(str, b_digits))
    carry_str = " ".join(map(str, carry[:-1]))
    result_str = " ".join(map(str, result))
  

    # Build display
    display = ""
    display += "Adding "+a_show+ " to " +b_show + "\n"    
    display += "  " + a_str + "\n"                # top number
    display += "+ " + b_str + "\n"               # bottom number with plus
    display += "  " + carry_str + "    " +"<-- carry"+"\n"           # carry directly under digits
    display += "-" * (len(result_str)+2) + "\n"  # separator
    display += "  " + result_str + "\n"                  # final result
    # Add step-by-step explanations
    if explanations:
        display += "Step-by-step explanations: (Column 1 being the rightmost column)\n"
        for e in explanations:
            display += "- " + e + "\n"
    display += "Final Answer = " + result_show
    return display
def generate_random_problem(num_digits: int = 7):
    """Generates two random integers with `num_digits` digits."""
    a = random.randint(10**(num_digits-1), 10**num_digits - 1)
    b = random.randint(10**(num_digits-1), 10**num_digits - 1)
    return a, b

def check_answer(user_input: int, correct_sum: int) -> bool:
    """Validates user's answer."""
    return user_input == correct_sum

# step = add_step_by_step(9279342, 4673562)
# print(format_steps(step))

# # Step 1: generate two numbers
# a, b = generate_random_problem(5)  # generates two 5-digit numbers
# print(f"Solve: {a} + {b}")

# # Step 2: calculate the correct sum
# step_dict = add_step_by_step(a, b)
# result = step_dict["result"]
# correct_sum = int("".join(map(str, result)))


# # Step 3: simulate a user's answer
# user_input = int(input("Your answer: "))

# # Step 4: check the answer
# if check_answer(user_input, correct_sum):
#     print("Correct! ✅")
# else:
#     print(f"Oops! The answer is wrong. ❌")
#     print(format_steps(step_dict))