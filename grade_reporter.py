# List and loop through it
scores = [72, 45, 90, 61, 38]

for score in scores:
    if score >= 80:
        print("A")
    elif score >= 70:
        print("B")
    elif score >= 50:
        print("C")

    else:
        print("F")

passed = 0
failed = 0
total = 0

for record in scores:
    total = total + 1
    if record >= 50:
        passed = passed + 1
    else:
        failed
        failed = failed + 1

average = total / len(scores)

# Print the results
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Average: {average:.1f}")