# This is the Python Essentials 2 LAB 4.1.1.2 Fibonacci generator

class Fib:
    def __init__(self, nn):
        # the class constructor. It prepares some variables.
        self.__n = nn             # to store the series limit
        self.__i = 0              # to track the current Fibonacci number to provide
        self.__p1 = self.__p2 = 1 # to save the two previous Fibonacci numbers

    def __iter__(self):
        # the __iter__ method is obliged to return the iterator object itself.
        return self

    def __next__(self):
        # the __next__ method is responsible for creating the sequence;
        self.__i += 1               # updates the number of desired values
        if self.__i > self.__n:     # if it reaches the end of the sequence ...
            raise StopIteration     # breaks the iteration by raising the StopIteration 
        # the following code precisely reflects the definition of the Fib numbers
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


# Main
if __name__ == "__main__":
    # make use of the iterator
    for i in Fib(10):
        print(i)
