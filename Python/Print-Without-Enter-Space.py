# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.

# Example
# n = 5
# Print the string 12345.

# Input Format
# The first line contains an integer n.
# Constraints: 1 <= n <= 150

# Output Format
# Print the list of integers from 1 through n as a string, without spaces.

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    


for x in range(1, n+1):
    print(x, end="")
