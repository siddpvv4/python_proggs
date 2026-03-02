#Write a Python function to find the maximum and minimum numbers from a sequence of numbers. (Note: Do not use built-in functions.)
def find_max_min(numbers):
    if len(numbers) == 0:
        return None
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    
    return maximum, minimum


# Example
nums = [10, 6, 8, 90, 12, 56]
print(find_max_min(nums))   # (90, 6)