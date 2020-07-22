#Given a binary array, find the maximum number of consecutive 1s in this array.

def maxones(input_array):
    count = 0
    maximum = 0
    for num in input_array:
        if num == 1:
            count += 1
            maximum = max(count, maximum)
        else:
            count = 0

    return maximum

#driver code


input_array = [1, 1, 0, 1, 1, 1]
print("The answer is " + str(maxones(input_array)))