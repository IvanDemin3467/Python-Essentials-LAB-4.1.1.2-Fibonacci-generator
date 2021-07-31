# This is the Python Essentials 2 LAB 4.1.1.5 Fibonacci generator v2

def fibonacci(n):
    # This is the Fibonacci number generator
    p = pp = 1            # Initialize two previous Fib numbers
    for i in range(n):    # Iterate to find next Fib numbers
        if i in [0, 1]:   # First two Fib nubmers are equal to 1
            yield 1       # Generate output
        else:             # Staring from the third number the formula is:
            n = p + pp    # Next number = previous number  + previous previous number 
            pp, p = p, n  # Forget previous previous number . Store next and previous numbers
            yield n       # Generate output


# Main
if __name__ == "__main__":
    # make use of the gererator
    fibs = list(fibonacci(10))
    print(fibs)
