This is the sample program for test

Que.-Write a single line python code to print prime numbers between 50 and 150.
please write the answers here only.
[print(x) for x in range(50, 150) if not list(filter(lambda y: (x % y) == 0, range(2, x - 1)))]