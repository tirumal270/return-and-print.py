
#Understanding the Difference Between print and return in Python Functions

def show_sum(a, b):
    print(a + b)


def get_sum(a, b):
    return a + b


def format_sum(a, b):
    result = a + b
    return f"Sum of {a} and {b} is {result}"




from printer import show_sum, get_sum, format_sum

# Task 1
show_sum(3, 5)

# Task 2
result = get_sum(3, 5)
print(result)

# Flags
USE_PRINT = True
USE_FORMAT = False

pairs = [(3, 5), (10, 20), (7, 8)]

if USE_PRINT:
    for a, b in pairs:
        show_sum(a, b)
else:
    results = []

    for a, b in pairs:
        if USE_FORMAT:
            results.append(format_sum(a, b))
        else:
            results.append(get_sum(a, b))

    print(results)
