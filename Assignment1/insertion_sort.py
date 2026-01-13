"""
Insertion Sort Algorithm - Monotonically Decreasing Order
MSCS 532 - Assignment 1

This program implements the Insertion Sort algorithm to sort an array
in decreasing order (from largest to smallest).

Algorithm Explanation:
- Time Complexity: O(n²) in worst case, O(n) in best case
- Space Complexity: O(1) - sorts in place
- Stable sorting algorithm
"""

def insertion_sort_decreasing(arr):
    """
    Sort an array in decreasing order using Insertion Sort.
    
    The algorithm works by iterating through the array and for each element,
    finding its correct position in the already sorted portion of the array.
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        The sorted array in monotonically decreasing order
    """
    # Start from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted in sorted portion
        j = i - 1
        
        # Move elements that are smaller than key to one position ahead
        # For decreasing order, we shift elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr


def print_test_case(test_name, original, sorted_arr):
    """Helper function to print test results in a formatted way."""
    print(f"\n{test_name}")
    print(f"Original: {original}")
    print(f"Sorted:   {sorted_arr}")


# Test the function with multiple test cases
if __name__ == "__main__":
    print("=" * 60)
    print("INSERTION SORT - DECREASING ORDER TEST CASES")
    print("=" * 60)
    
    # Test Case 1: Regular unsorted array
    test1 = [5, 2, 4, 6, 1, 3]
    result1 = insertion_sort_decreasing(test1.copy())
    print_test_case("Test 1: Regular Array", [5, 2, 4, 6, 1, 3], result1)
    
    # Test Case 2: Already sorted in decreasing order
    test2 = [9, 7, 5, 3, 1]
    result2 = insertion_sort_decreasing(test2.copy())
    print_test_case("Test 2: Already Sorted (Decreasing)", [9, 7, 5, 3, 1], result2)
    
    # Test Case 3: Sorted in increasing order (worst case)
    test3 = [1, 2, 3, 4, 5]
    result3 = insertion_sort_decreasing(test3.copy())
    print_test_case("Test 3: Sorted Increasing (Worst Case)", [1, 2, 3, 4, 5], result3)
    
    # Test Case 4: Array with duplicates
    test4 = [5, 2, 8, 2, 9, 1, 5]
    result4 = insertion_sort_decreasing(test4.copy())
    print_test_case("Test 4: Array with Duplicates", [5, 2, 8, 2, 9, 1, 5], result4)
    
    # Test Case 5: Single element
    test5 = [42]
    result5 = insertion_sort_decreasing(test5.copy())
    print_test_case("Test 5: Single Element", [42], result5)
    
    # Test Case 6: Large numbers
    test6 = [100, 45, 789, 23, 456]
    result6 = insertion_sort_decreasing(test6.copy())
    print_test_case("Test 6: Large Numbers", [100, 45, 789, 23, 456], result6)
    
    # Test Case 7: Negative numbers
    test7 = [-5, 3, -1, 7, -9, 2]
    result7 = insertion_sort_decreasing(test7.copy())
    print_test_case("Test 7: Negative Numbers", [-5, 3, -1, 7, -9, 2], result7)
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)