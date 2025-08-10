def is_power_of_two_bitwise(n: int) -> bool:
    """
    Check if n is a power of two using bitwise operation.
    Returns True if n is a power of two, else False.
    """
    return n > 0 and (n & (n - 1)) == 0


def is_power_of_two_loop(n: int) -> bool:
    """
    Check if n is a power of two by repeatedly dividing by 2.
    Returns True if n is a power of two, else False.
    """
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1


def main():
    test_cases = [1, 16, 3, 0, -4, 1024, 1023]

    print("Testing is_power_of_two_bitwise:")
    for n in test_cases:
        print(f"n = {n}: {is_power_of_two_bitwise(n)}")

    print("\nTesting is_power_of_two_loop:")
    for n in test_cases:
        print(f"n = {n}: {is_power_of_two_loop(n)}")


if __name__ == "__main__":
    main()
