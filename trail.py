


def countBits(num):
    counter = [0]  # Initialize the list with the count for 0, which is 0
    for i in range(1, num + 1):  # Iterate from 1 to num (inclusive)
        # Calculate the number of 1-bits for the current number
        counter.append(counter[i >> 1] + i % 2)
    return counter  # Return the list with counts for each number




print(countBits(7))