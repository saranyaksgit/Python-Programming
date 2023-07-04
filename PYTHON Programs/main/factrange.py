def factorsInRange(start, end):
    for num in range(start, end+1):
        factors = []
        for i in range(1, num+1):
            if num % i == 0:
                factors.append(i)
        print("Factors of", num, "are:", factors)

# Example usage:
factorsInRange(10, 20)

