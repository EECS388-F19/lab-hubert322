import random

print("Hubert Tzu-Fan Hung")

randomNums = []
for i in range(0, 2):
    randomNums.append(random.randint(0, 100))
    print(randomNums[i])

sum = randomNums[0] + randomNums[1]
print(f"Sum = {sum}")
print(f"Average = {float(sum) / 2}")