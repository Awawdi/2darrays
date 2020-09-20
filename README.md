# 2darrays
Context
Given a 2D Array 6x6

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A , then print the maximum hourglass sum.

Input Format

There are 6 lines of input, where each line contains space-separated integers describing 2D Array A ; 
every value in A will be in the inclusive range of -9 to +9

Output Format

Print the largest (maximum) hourglass sum found in A.
