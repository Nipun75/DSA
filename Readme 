# DSA Topics

## 1. Two Pointer Technique

The **Two Pointer Technique** is a common approach used in arrays and strings to optimize brute-force solutions by maintaining two indices (pointers) that move according to specific conditions.

### A. Array Traversal from Both Ends

**Template:**

```python
left = 0
right = len(arr) - 1

while left < right:
    if condition_1:
        left += 1
        right -= 1
    elif condition_2:
        left += 1
    else:
        right -= 1
```

**Common Use Cases:**
- Two Sum (sorted array)
- Array Reversal
- Sort Colors (Dutch National Flag variant)
- Reversing an array
---

### B. Array Traversal from One End

**Template:**

```python
left = 0
right = 0
n = len(arr)

while left < n:
    if condition:
        right += 1

    left += 1
```

**Common Use Cases:**
- Sliding Window problems
- Removing duplicates in sorted arrays
- Merging two sorted arrays
- Counting subarrays satisfying a condition

---

### Key Idea

- Use **two indices** instead of nested loops.
- Move pointers based on the problem constraints.
- Often reduces time complexity from **O(n²)** to **O(n)**.

### Recognition Pattern

Consider the Two Pointer Technique when:
- The input is an array or string or linked list. 
- The problem involves pairs,triplets, ranges, or subarrays.
- The array is sorted (very common).
- You need an optimal linear-time and constant space solution 
- There is a possibility that the question mentions rearrange/remove/merge/duplicate