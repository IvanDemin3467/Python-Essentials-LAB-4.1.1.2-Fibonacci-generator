# Python-Essentials-LAB-4.1.1.2-Fibonacci-generator
A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process.

You should build a class able to iterate through the first n values (where n is a constructor parameter) of the Fibonacci numbers.

Let us remind you - the Fibonacci numbers (Fibi) are defined as follows:

Fib_1 = 1

Fib_2 = 1

Fib_i = Fib_i-1 + Fib_i-2

In other words:

•	the first two Fibonacci numbers are equal to 1;

•	any other Fibonacci number is the sum of the two previous ones (e.g., Fib3 = 2, Fib4 = 3, Fib5 = 5, and so on)

**Completed. The code v1 uses direct iterator protocol implementation:**
```
class Fib:
    def __init__(self, nn):
        # the class constructor. It prepares some variables.

    def __iter__(self):
        # the __iter__ method is obliged to return the iterator object itself.

    def __next__(self):
        # the __next__ method is responsible for creating the sequence;
```

**The code v2 implements generator as it is**
```
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
```
