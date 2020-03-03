
def polindrome(size):
    '''
    (int) -> int

    Function returns the largest palindrome, that can be
    expressed as the multiple of 2 numbers with number of digits = size in each

    '''

    
    x = (10**size) - 1 # largest size-digit
    y = (10**size) - 1
    z = 10**(size-1)
    all_polindromes = [] # smallest size-digit number
    
    for i in (a*b for a in range(x,z, -1) for b in range(y, z, -1)):
        number = list(str(i))
        
        first_half = number[:size]
        second_half = number[size:]
        second_half.reverse()

        if first_half == second_half:
            
            all_polindromes.append(i)
    print(all_polindromes)
    all_polindromes.sort()
    
    if len(all_polindromes)!=0:
        return all_polindromes[-1]
    else:
        return "no polindromes found"
