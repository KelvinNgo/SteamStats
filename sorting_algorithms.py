

def low_high_merge(left, right):
    """Merge two lists into a single list ordered lowest to highest."""
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left]["percentcomplete"] <= right[index_right]["percentcomplete"]:
            result.append(left[index_left])
            index_left += 1

        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def high_low_merge(left, right):
    """Merge two lists into a single list ordered highest to lowest."""
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left]["percentcomplete"] >= right[index_right]["percentcomplete"]:
            result.append(left[index_left])
            index_left += 1

        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort_low_high(array):
    """Split given list in half and sort recursively lowest to highest."""
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return low_high_merge(left=merge_sort_low_high(array[:midpoint]), right=merge_sort_low_high(array[midpoint:]))


def merge_sort_high_low(array):
    """Split given list in half and sort recursively lowest to highest."""
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return high_low_merge(left=merge_sort_high_low(array[:midpoint]), right=merge_sort_high_low(array[midpoint:]))
