def reorderedPowerOf2(n: int) -> bool:
    target = ''.join(sorted(str(n)))
    for i in range(31):
        if ''.join(sorted(str(1 << i))) == target:
            return True
    return False

if __name__ == "__main__":
    print(reorderedPowerOf2(1))   # True
    print(reorderedPowerOf2(10))  # False

