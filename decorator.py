def decorator(f):
    def wrapper(n):
        return f'The square of {n} is: {f(n)}\n'

    return wrapper


@decorator
def square(n):
    return n ** 2


def main():
    print(square(7))


if __name__ == '__main__':
    main()
