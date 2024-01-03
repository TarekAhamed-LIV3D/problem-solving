def mySqrt(x):
    if x == 0 or x == 1:
        return x

    left, right = 1, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

num = 75
result = mySqrt(num)
print("Square root of", num, "rounded down:", result)
