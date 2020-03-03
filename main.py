
def polindrome(size):
    '''
    (int) -> int

    Function returns the largest palindrome, that can be
    expressed as the multiple of 2 numbers with number of digits = size in each

    '''

    
    x = (10**size) - 1 # largest size-digit
    z = 10**(size-1)
    
    all_polindromes = [] # smallest size-digit number
    
    for i in (a*b for a in range(z,x) for b in range(a, x)):
        number = list(str(i))
        
        first_half = number[:size]
        second_half = number[size:]
        second_half.reverse()

        if first_half == second_half:
            
            all_polindromes.append(i)
    
    all_polindromes.sort()

    if len(all_polindromes)!=0:
        return all_polindromes[-1]
    else:
        return "no polindromes found"
