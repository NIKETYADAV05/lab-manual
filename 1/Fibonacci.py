# Fibonacci Series up to n terms


def fibonacci_series(n):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")

    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    n = int(input("Enter the number of terms: "))
    print(fibonacci_series(n))


if __name__ == "__main__":
    main()
