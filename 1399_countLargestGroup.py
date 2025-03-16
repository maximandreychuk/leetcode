def countLargestGroup(n):
    digit_sums = {}  # Dictionary to store digit sums and their counts
    max_size = 0     # Variable to track the maximum group size

    for i in range(1, n + 1):
        digit_sum = sum(map(int, str(i)))  #Efficiently calculate digit sum
        digit_sums[digit_sum] = digit_sums.get(digit_sum, 0) + 1
        max_size = max(max_size, digit_sums[digit_sum])

    count_max_size = sum(1 for count in digit_sums.values() if count == max_size)
    return count_max_size

print(countLargestGroup(13))