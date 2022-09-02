with open("file1.txt") as f1:
    number1 = [int(num.strip()) for num in f1.readlines()]

with open("file2.txt") as f2:
    number2 = [int(num.strip()) for num in f2.readlines()]

result = [n for n in number1 if n in number2]

print(result)
