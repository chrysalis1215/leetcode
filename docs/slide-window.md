✅ What is Sliding Window?

Sliding window is a technique used to reduce nested loops when searching or processing subarrays/substrings of fixed or dynamic size.

⸻

🧱 Types of Sliding Windows

|Type|	Description	Example Problem|
| -------- | ------- |
|Fixed-size window|Window size stays constant|	Max sum of subarray of size k|
|Variable-size window|	Window grows/shrinks to fit condition|	Longest substring without repeating chars


⸻

🔧 Common Template (Variable-size window)

left = 0
for right in range(len(s)):
    # expand the window

    while window is invalid:
        # shrink from the left
        left += 1

    # update result if needed
⸻

🧪 Beginner Sliding Window Problems to Practice

1. Fixed-size Window 
   - leetCode 209: Minimum Size Subarray Sum 
   - LeetCode 643: Maximum Average Subarray I

2. Variable-size Window
   - leetCode 3: Longest Substring Without Repeating Characters
   - leetCode 76: Minimum Window Substring
   - leetCode 567: Permutation in String


🧠 Key Skills to Learn
    - How to expand and shrink the window
    - How to track things like:
    - frequency of characters
    - number of distinct characters
    - sum of elements in window
    - When to update your result (max/min/length/etc.)

