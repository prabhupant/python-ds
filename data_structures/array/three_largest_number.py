def three_largest(arr):
    result = ""
    for _ in range(3):
        maximum = float('-inf')
        for element in arr:
            if(maximum < element):
                maximum = element
        result += str(maximum) + " "
        arr.remove(maximum)
    return result

arr = [10,45,3,7,4,6,8,9,4,6,4,23,45,56,47,25,34,67,634]
print(three_largest(arr))
