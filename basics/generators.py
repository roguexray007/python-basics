# Key Benefits of Generators:
# Memory Efficiency: They generate values on-demand rather than storing them all in memory
# Lazy Evaluation: Values are computed only when needed
# Infinite Sequences: Can represent infinite sequences without infinite memory
# State Maintenance: Can maintain state between iterations


def myGenerator():
    print("starting generator")
    yield 1
    print("after first yield")
    yield 2
    print("after second yield")
    yield 3
    print("after third yield")


gen = myGenerator()
print("generator created")


# First call
print("First next() call:")
print(next(gen))  # Prints: "Starting generator" then "1"

# Second call
print("\nSecond next() call:")
print(next(gen))  # Prints: "After first yield" then "2"

# Third call
print("\nThird next() call:")
print(next(gen))  # Prints: "After second yield" then "3"