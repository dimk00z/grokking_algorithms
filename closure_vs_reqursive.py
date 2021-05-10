from utils import measure


@measure
def recursive_fib(n):
    def fib(n):
        if n in (1, 2):
            return 1
        return fib(n-1)+fib(n-2)
    return fib(n)


@measure
def closure_fib(n, start=(1, 2)):

    x1, x2 = start

    def get_next_number():
        nonlocal x1, x2
        x3 = x2 + x1
        x1, x2 = x2, x3
        return x3
    result = step = 1
    while step < (n-2):
        result = get_next_number()
        step += 1
    return result


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


def main():
    print(recursive_fib(20))
    print(closure_fib(20))
    try:
        print(simple_recursive_factorial(1000))
    except RecursionError as ex:
        print(ex)
    print(closure_factorial(1000))


if __name__ == "__main__":
    main()
