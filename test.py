def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Test the function
if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 10, 17, 20, 29]
    for num in numbers:
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
