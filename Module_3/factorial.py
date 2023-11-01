def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))



    
    
    
    