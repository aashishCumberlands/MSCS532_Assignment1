# MSCS532_Assignment1
Insertion Sort Algorithm - Monotonically Decreasing Order

## Overview
This repository contains an implementation of the Insertion Sort algorithm that sorts arrays in **monotonically decreasing order** (from largest to smallest).

## Author
Aashish Sapkota
University of the Cumberlands  
MSCS 532 - Data Structures and Algorithms

## Algorithm Description
Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works by:
1. Iterating through the array starting from the second element
2. Comparing each element with the elements in the already-sorted portion
3. Inserting the element in its correct position

### Complexity
- **Time Complexity**: 
  - Best Case: O(n) - when array is already sorted
  - Average Case: O(n²)
  - Worst Case: O(n²) - when array is sorted in reverse
- **Space Complexity**: O(1) - sorts in place

## Files
- `insertion_sort.py` - Main implementation with multiple test cases

## How to Run
1. Ensure Python 3.8+ is installed
2. Clone this repository
3. Run the program:
```bash
   python insertion_sort.py
```

## Test Cases
The program includes 7 comprehensive test cases:
1. Regular unsorted array
2. Already sorted in decreasing order
3. Sorted in increasing order (worst case)
4. Array with duplicate values
5. Single element array
6. Large numbers
7. Negative numbers

## Example Output
```
Original: [5, 2, 4, 6, 1, 3]
Sorted:   [6, 5, 4, 3, 2, 1]
```

## Development Process
This project was developed with version control best practices:
- Commit 1: Initial file structure and function signature
- Commit 2: Core algorithm implementation
- Commit 3: Comprehensive testing and documentation

## References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
```

