handle = open("numbers.txt")
text = handle.read()
num_sum = sum(map(int, text.split('\n')))
print(num_sum)