def factors_in_range(start, end):
    for i in range(start, end+1):
        print("Factors of", i, ":", end=" ")
        for j in range(1, i+1):
            if i % j == 0:
                print(j, end=" ")
        print()

factors_in_range(1, 10)

