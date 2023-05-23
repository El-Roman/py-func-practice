# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(max_num(3,5,2))



# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(l):
    res=1
    for i in l:
        res=res*i
    return res

print(mult_list([1,2,3]))




# Write a Python function called rev_string() to reverse a string.
def rev_string(s):
    return s[::-1]

print(rev_string("orange chicken"))



# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(n,a,b):
    if n>=a and n<=b:
        return True
    else:
        return False
    
print(num_within(3,2,4))




# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print()

pascal(5)




