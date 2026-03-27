from addition_tutor import add_step_by_step,format_steps


def add_with_steps(a: int, b: int, show_carry: bool = True) -> str:
    """
    High-level function to add two integers step-by-step.
    
    Returns a nicely formatted string showing:
    - aligned digits
    - carries
    - result
    - step-by-step explanations
    """
    # Step 1: compute addition steps
    steps = add_step_by_step(a, b, show_carry=show_carry)
    
    # Step 2: format them into a readable string
    formatted = format_steps(steps)
    
    return formatted

print(add_with_steps(123,234))