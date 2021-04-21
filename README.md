# Reorder-Characters-Of-A-String
Reorder characters of a string to valid English representations of digits

Given a string S of length N, consisting of lowercase characters containing reordered English representations of digits [0 – 9], the task is to print those digits in ascending order.

Examples:

Input: S = “fviefuro”
Output: 45
Explanation: The given string can be reshuffled to “fourfive”, Therefore, the digits represented by the strings are 4 and 5.

Input: S = “owoztneoer”
Output: 012
Explanation: The given string can be reshuffled to get “zeroonetwo”, Therefore, the digits represented by the strings are 0, 1 and 2.

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Naive Approach: The simplest approach is to generate all permutations of the given string and for each permutation, check if it is possible to find valid digits represented by the string. If found to be true, then print the set of digits in ascending order.


Time Complexity: O(N * N!)
Auxiliary Space: O(1)

Efficient Approach: The idea is based on the observation that some characters only appear in one number.

In ‘zero’, character ‘z’ is unique.
In ‘two’, character ‘w’ is unique.
In ‘four’, character ‘u’ is unique.
In ‘six’, character ‘x’ is unique.  
In ‘eight’, character ‘g’ is unique.
In ‘three’, character ‘h’ is unique since word “eight” having character ‘h’ has already been considered.
In ‘one’, character ‘o’ is unique since words having character ‘o’ have already been considered.
In ‘five’, character f’ is unique since word “four” having character ‘f’ has already been considered.
In ‘seven’, character ‘v’ is unique.
In ‘nine’, character ‘i’ is unique since words having character ‘i’ have already been considered.

Follow the steps below to solve the problem:

  * Initialize an empty string, ans to store the required result.
  * Store the frequency of each character of the string in M.
  * Create a mapping of a unique character to its corresponding string.
  * Traverse the map, and perform the following steps:
    * Store the unique character corresponding to the digit in a variable x.
    * Get the occurrence of x in M, and store it in a variable freq.
    * Append the corresponding digit, freq number of times to ans.
    * Traverse the word corresponding to x and decrement the frequency of its characters by freq in M.
  * Print the string, ans as the result. 
