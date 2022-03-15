"""List Pratice."""

a: int = 3
b: int = 0
c: float


def main() -> None:
    """Entry point of program."""
    global a
    global b
    print(fun(a, b))


def fun(a: int, b: int) -> list[int]:
    """A sample function."""
    global c
    nums: list[int] = []
    if b == 0:
        while len(nums) < 4:
            c = a + b / 2
            if c % 2 == 0:
                a += 1
                b += 1
            else:
                nums.append(a)
                a += 3
    return nums


if __name__ == "__main__":
    main()