def generate_quicksort_best_case(n):
    """
    Generates an array of numbers from 1 to n arranged so that 
    the median is always chosen first, guaranteeing O(n log n) for QuickSort.
    """
    def build_best_case(low, high):
        if low > high:
            return []
        
        # Find the middle value
        mid = (low + high) // 2
        
        # Put the middle value FIRST, then process the left and right halves
        left_half = build_best_case(low, mid - 1)
        right_half = build_best_case(mid + 1, high)
        
        return [mid] + left_half + right_half

    return build_best_case(1, n)

print("QuickSort Best Case: " + str(generate_quicksort_best_case(100)))
# Example: n = 7
# Output: [4, 2, 1, 3, 6, 5, 7]

def generate_quicksort_worst_case(n):
    """
    Generates an array of numbers from 1 to n arranged in sorted order,
    which is the worst case for QuickSort when the first or last element is chosen as pivot.
    """
    return list(range(1, n + 1))

# print("QuickSort Worst Case: " + str(generate_quicksort_worst_case(7)))
# Example: n = 7
# Output: [1, 2, 3, 4, 5, 6, 7]

def generate_quicksort_average_case(n):
    """
    Generates an array of numbers from 1 to n in random order,
    which represents the average case for QuickSort.
    """
    import random
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr

# print("QuickSort Average Case: " + str(generate_quicksort_average_case(7)))
# Example: n = 7
# Output: [3, 1, 4, 2, 6, 7, 5] (random order)

def generate_merge_best_case(n):
    """
    Generates an array of numbers from 1 to n arranged in sorted order,
    which is the best case for MergeSort.
    """
    return list(range(1, n + 1))

def generate_merge_worst_case(n):
    """
    Generates an array of numbers from n to 1 arranged in reverse order,
    which is the worst case for MergeSort.
    """
    return list(range(n, 0, -1))

def generate_merge_average_case(n):
    """
    Generates an array of numbers from 1 to n in random order,
    which represents the average case for MergeSort.
    """
    import random
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr