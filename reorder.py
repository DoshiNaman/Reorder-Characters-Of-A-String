# Python program to implement the above approach
from collections import Counter

# Function to construct the original set of digits
# from the string in ascending order
def construct_digits(s):

	# Store the unique characters
	# corresponding to word and number
	k = ["z", "w", "u", "x", "g",
		"h", "o", "f", "v", "i"]

	l = ["zero", "two", "four", "six", "eight",
		"three", "one", "five", "seven", "nine"]

	c = [0, 2, 4, 6, 8, 3, 1, 5, 7, 9]
	
	# Store the required result
	ans = []
	
	# Store the frequency of
	# each character of S
	d = Counter(s)

	# Traverse the unique characters
	for i in range(len(k)):

		# Store the count of k[i] in S
		x = d.get(k[i], 0)
		
		# Traverse the corresponding word
		for j in range(len(l[i])):
			
			# Decrement the frequency
			# of characters by x
			d[l[i][j]]-= x
			
		# Append the digit x times to ans
		ans.append(str(c[i])*x)

	# Sort the digits in ascending order
	ans.sort()

	return "".join(ans)

# Driver Code

# Given string, s
s = "fviefuro"

# Function Call
print(construct_digits(s))

#this code made by 'naman_d0shi'
