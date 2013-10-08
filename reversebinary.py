from sys import stdin

"""
https://www.spotify.com/us/jobs/tech/reversed-binary/
Spotify Puzzle -- Reversed Binary Numbers
Problem ID: reversebinary

Your task will be to write a program for reversing numbers in binary. For
instance, the binary representation of 13 is 1101, and reversing it gives 1011,
which corresponds to number 11.

The input contains a single line with an integer N, 1 ≤ N ≤ 1000000000.

Output one line with one integer, the number we get by reversing the binary
representation of N.
"""

arg = int(stdin.readline())
bin = bin(arg)[2:]
dec = int(bin[::-1], 2)
print dec
