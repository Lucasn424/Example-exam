'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).




'''

# Write a function with two inputs, one matrix (a list of lists, in which every sublist is the same dimension)
# and a single character. The function will return true if it can find, within the matrix, a 2x2 submatrix made
# with the single character.
#
# Example: Consider the following list, myList = [[1,2,"a","a"], ["a", 3, "a", "a"], [1, 4, 6, 8], [5, 2, 6, 6]]
# that corresponds to the following matrix
# 
#
#
# |  1   2  "a" "a"  |
# | "a"  3  "a" "a"  |
# |  1   4   6   8   |
# |  5   2   6   6   |
#
# in which case the function would return True, if the character was "a" and false otherwise.
# weight = 15

def find_letter():
    return




def find_letter():
    return


# Python 3 program to find 
# maximum K such that K x K
# is a submatrix with equal 
# elements.
Row = 6
Col = 6
  
# Returns size of the 
# largest square sub-matrix
# with all same elements.
def largestKSubmatrix(a):
    dp = [[0 for x in range(Row)]
             for y in range(Col)]
  
    result = 0
    for i in range(Row ):
        for j in range(Col):
              
            # If elements is at top 
            # row or first column, 
            # it wont form a square
            # matrix's bottom-right
            if (i == 0 or j == 0):
                dp[i][j] = 1
  
            else:
                  
                # Check if adjacent 
                # elements are equal
                if (a[i][j] == a[i - 1][j] and
                    a[i][j] == a[i][j - 1] and
                    a[i][j] == a[i - 1][j - 1]):
                      
                    dp[i][j] = min(min(dp[i - 1][j], 
                                       dp[i][j - 1]),
                                       dp[i - 1][j - 1] ) + 1
  
                # If not equal, then  
                # it will form a 1x1
                # submatrix
                else:
                    dp[i][j] = 1
  
            # Update result at each (i,j)
            result = max(result, dp[i][j])
              
    return result
  
# Driver Code
a = [[ 2, 2, 3, 3, 4, 4],
     [ 5, 5, "a", "a", "a", 7],
     [ 1, 2, "a", "a", "a", 7],
     [ 4, 4, "a", "a", "a", 7],
     [ 5, 5, "a", "a", "a", 7],
     [ 8, 7, 9, 4, 4, 4]];
  
print(largestKSubmatrix(a))


  
# This code is contributed
# by ChitraNayal