# Normal way
numbers = []
for i in range(1,6):
    numbers.append(i)
print(numbers)

# Comprehensive way - one line
numbers = [i for i in range(1,6)]
print(numbers) # [1,2,3,4,5]

# Even Numbers
evens = [i for i in range(1,11) if i % 2 == 0]
print(evens) # [2,4,6,8,10]

# Squares
squares = [i*i for i in range(1,6)]
print(squares) # [1,4,9,10,25]