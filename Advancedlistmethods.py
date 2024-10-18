# Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

alice_submitted = "Alice" in submitted
alice_attended ="Alice" in attended
print("Alice submitted:", alice_submitted)
print("Alice attended:", alice_attended)

not_attended = [student for student in submitted if student not in attended]
print("Submitted but not attended:", not_attended)

not_submitted = [student for student in attended if student not in submitted]
print("Attended but not submitted:", not_submitted)