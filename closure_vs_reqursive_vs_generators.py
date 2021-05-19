from utils import measure


@measure
def recursive_fib(n):
    def fib(n):
        if n in (1, 2):
            return 1
        return fib(n-1)+fib(n-2)
    return fib(n)


@measure
def closure_fib(n, start=(0, 1)):

    x1, x2 = start
    result = 0

    def get_next_number():
        nonlocal x1, x2
        x3 = x2 + x1
        x1, x2 = x2, x3
        return x3
    step = 1
    while step < (n):
        result = get_next_number()
        step += 1
    return result


@measure
def fib_with_generators(n):
    def fib(n):
        a, b = 0, 1
        for _ in range(n+1):
            yield a
            a, b = b, a+b
    return tuple(fib(n))[-1]


@measure
def simple_recursive_factorial(value):
    def factorial(value):
        return 1 if value == 1 else value*factorial(value-1)
    return factorial(value)


@measure
def closure_factorial(value):
    result = 1
    steps = value

    def factorial(step):
        nonlocal result
        result = result*step
        return result
    for step in range(1, steps+1):
        result = factorial(step)
    return result


@measure
def factorial_with_generators(value):
    def factorial(value):
        result = 1
        for step in range(1, value+1):
            result *= step
            yield(result)
    return tuple(factorial(value))[-1]


def main():
    value = 10000
    # fib
    try:
        print(recursive_fib(value))
    except RecursionError as ex:
        print(ex)
    print(closure_fib(value))
    print(fib_with_generators(value))

    # factorial
    try:
        print(simple_recursive_factorial(value))
    except RecursionError as ex:
        print(ex)

    print(closure_factorial(value))
    print(factorial_with_generators(value))


if __name__ == "__main__":
    main()
