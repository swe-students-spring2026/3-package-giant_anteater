# Step 1: generate two numbers
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