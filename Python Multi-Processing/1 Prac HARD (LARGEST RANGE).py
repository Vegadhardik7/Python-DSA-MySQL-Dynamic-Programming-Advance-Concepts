def largestRange(array):
    numbers = {x:0 for x in array}
    left = right = 0

    for num in array:
        if numbers[num] == 0:
            left_cnt = num - 1
            right_cnt = num - 1

            # Lookup in HASH Table
            while left_cnt in numbers:
                numbers[left_cnt] = 1
                left_cnt -= 1
            left_cnt += 1

            while right_cnt in numbers:
                numbers[right_cnt] = 1
                right_cnt += 1
            right_cnt -=1

        if right-left<(right_cnt-left_cnt):
            right = right_cnt
            left = left_cnt

    return [left,right]

value = [0,3,2,1,7,11,4]

x = largestRange(value)
print(x)