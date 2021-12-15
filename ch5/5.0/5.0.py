'''
Question:
Input is an array of random sequence of numbers
You have to reorder its entries so that even entries appear first
Do it without using an additional storage

Time  Complexity: O(n)
Space Complexity: O(1)


'''

def even_odd(A):
    even_pointer, odd_pointer = 0, len(A)-1 

    while even_pointer < odd_pointer:
        if A[even_pointer] % 2 == 0:
            even_pointer += 1
        else:
            A[even_pointer], A[odd_pointer] = A[odd_pointer], A[even_pointer]
            odd_pointer -=1
    
    return A