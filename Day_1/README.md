# DSA Progress Log

## Problem Solved: Two Sum

Today, I solved the **Two Sum** problem using three different approaches:

1. Naive (Brute Force) Approach
2. HashMap Approach
3. Two Pointer Approach

**LeetCode Problem:** Two Sum
https://leetcode.com/problems/two-sum/

---

## 1. Naive (Brute Force) Approach

### Idea
Check every possible pair of elements and see if their sum equals the target.

### Algorithm
- Use two nested loops.
- For each element, compare it with all remaining elements.
- Return the indices when the target sum is found.

### Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time Complexity | O(n²) |
| Space Complexity | O(1) |

### Pros
- Simple and easy to understand.
- No extra data structures required.

### Cons
- Inefficient for large inputs due to quadratic time complexity.

---

## 2. HashMap Approach

### Idea
Store previously visited numbers in a hash map and check whether the complement exists.

**Complement = Target - Current Element**

### Algorithm
- Traverse the array once.
- For each element:
  - Compute its complement.
  - Check if the complement already exists in the hash map.
  - If found, return the indices.
  - Otherwise, store the current element and its index.

### Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time Complexity | O(n) |
| Space Complexity | O(n) |

### Pros
- Optimal time complexity.
- Works on unsorted arrays.

### Cons
- Requires extra memory.

---

## 3. Two Pointer Approach

### Idea
Use two pointers starting from both ends of a **sorted array**.

### Algorithm
1. Sort the array (while preserving original indices if needed).
2. Initialize:
   - `left = 0`
   - `right = n - 1`
3. Calculate the sum:
   - If sum == target → answer found.
   - If sum < target → move `left`.
   - If sum > target → move `right`.

### Complexity Analysis

| Metric | Complexity |
|----------|------------|
| Time Complexity | O(n log n) *(due to sorting)* |
| Space Complexity | O(1) or O(n) *(depending on implementation)* |

### Pros
- Very efficient after sorting.
- Uses minimal extra memory.
- Excellent for sorted-array problems.

### Cons
- Requires a sorted array.
- Original indices become difficult to track after sorting.

---

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Naive (Brute Force) | O(n²) | O(1) |
| HashMap | O(n) | O(n) |
| Two Pointer | O(n log n) | O(1) / O(n) |

---

## Why is the Two Pointer Approach Powerful?

The Two Pointer Technique is often considered one of the most important array patterns because:

- Eliminates unnecessary comparisons.
- Uses constant extra space in many problems.
- Converts many O(n²) solutions into O(n).
- Works exceptionally well on sorted arrays.
- Forms the foundation for advanced techniques such as:
  - Sliding Window
  - Fast & Slow Pointers
  - Merge Operations
  - Partitioning Algorithms



The **Two Pointer approach becomes preferable when:**
- The array is already sorted.
- Memory usage is a concern.
- The problem specifically allows sorting.
- Similar sorted-array problems need to be solved efficiently.

---

## Key Takeaway

For **Two Sum**:

- Brute Force → Easy but slow.
- HashMap → Best for unsorted arrays.
- Two Pointer → Best pattern for sorted arrays and many related array problems.

Understanding all three approaches helps build strong problem-solving intuition and prepares you for a wide variety of array-based interview questions.