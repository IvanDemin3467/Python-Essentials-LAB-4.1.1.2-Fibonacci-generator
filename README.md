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

**Completed. The code includes:**
```
class Fib:
    def __init__(self, nn):
        # the class constructor. It prepares some variables.

    def __iter__(self):
        # the __iter__ method is obliged to return the iterator object itself.

    def __next__(self):
        # the __next__ method is responsible for creating the sequence;
```
