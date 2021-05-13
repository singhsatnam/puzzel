def maxWater(arr, n):
    print("input: ", arr)
    left = 0
    right = n - 1

    l_max = r_max = 0
    result = 0

    while (left <= right):

        # We need check for minimum of left
        # and right max for each element
        print("////// r_max=", r_max, "l_max=", l_max, " leftPos=", arr[left], " rightPos=", arr[right])
        if r_max <= l_max:

            # Add the difference between
            # current value and right max at index r
            curr_water = max(0, r_max - arr[right])
            print("curr_water_if: ", curr_water, " r_max:", r_max, " - arr[right]:", arr[right])
            result += max(0, r_max - arr[right])

            # Update right max
            r_max = max(r_max, arr[right])
            print("updated r_max:", r_max)

            # Update right pointer
            right -= 1
        else:

            # Add the difference between
            # current value and left max at index l
            curr_water = max(0, l_max - arr[left])
            print("curr_water_else: ", curr_water, " l_max:", l_max, " - arr[left]:", arr[left])
            result += max(0, l_max - arr[left])

            # Update left max
            l_max = max(l_max, arr[left])
            print("updated l_max: ", l_max)

            # Update left pointer
            left += 1
    return result


# Driver code
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr = [2, 0, 1, 0, 3]
n = len(arr)
print(maxWater(arr, n))
