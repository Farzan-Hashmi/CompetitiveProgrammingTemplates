# This is terrible. I should be able to logic this out in like 5 seconds but alas.


from bisect import bisect_left, bisect_right


def next_smaller(arr, value):
    """Return strictly smaller value to the given value."""
    i = bisect_left(arr, value) - 1
    if i < 0:
        return None
    return arr[i]

def floor(arr, value):
    """Return smaller or equal value than the given value."""
    i = bisect_right(arr, value) - 1
    if i < 0:
        return None
    return arr[i]

def ceil(arr, value):
    """Return larger or equal value than the given value."""
    i = bisect_left(arr, value)
    if i >= len(arr):
        return None
    return arr[i]

def next_greater(arr, value):
    """Return strictly larger value than the given value."""
    i = bisect_right(arr, value)
    if i >= len(arr):
        return None