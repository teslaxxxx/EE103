start = int(input("Enter start: "))
end = int(input("Enter end: "))

result_for = 1

for i in range(start, end + 1):
    result_for *= i

result_while = 1
i = start

while i <= end:
    result_while *= i
    i += 1

print("For result:", result_for)
print("While result:", result_while)

if result_for == result_while:
    print("results are same")
else:
    print("results are different")

