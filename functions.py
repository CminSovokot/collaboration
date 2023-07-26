def multiply(a: int, b: int) -> int:
    return b*a

def summator(a: int, b: int) -> int:
    return a+b


if __name__ == '__main__':
    c: int = summator(5, 6)
    print(c)
    c = multiply(5, 6)
    print(c)
