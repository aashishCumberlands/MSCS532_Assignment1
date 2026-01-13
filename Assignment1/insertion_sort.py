"""
Insertion Sort Algorithm - Monotonically Decreasing Order
MSCS 532 - Assignment 1

This program implements the Insertion Sort algorithm to sort an array
in decreasing order (from largest to smallest).
"""

def insertion_sort_decreasing(arr):
    """
    Sort an array in decreasing order using Insertion Sort.
    
    Args:
        arr: List of numbers to be sorted
        
    Returns:
        The sorted array in decreasing order
    """
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        
        # Move elements that are smaller than key to one position ahead
        # For decreasing order, we move elements smaller than key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr


# Test the function
if __name__ == "__main__":
    test_array = [5, 2, 4, 6, 1, 3]
    print("Original array:", test_array)
    
    sorted_array = insertion_sort_decreasing(test_array.copy())
    print("Sorted array (decreasing):", sorted_array)